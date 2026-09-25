"""Check a bilingual static portfolio site without network or third-party packages."""
from __future__ import annotations

import hashlib
import json
import re
import struct
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

site = Path(__file__).resolve().parents[1]
workspace = site.parent
pages = [site / "index.html", site / "pt" / "index.html"]
evidence = json.loads((site / "evidence.json").read_text(encoding="utf-8"))
repo_folders = {
    "eng_dados-analytics_engineering": "airbnb-rio",
    "ML_olympiad_for_students-topvistos_EUA": "kaggle-topvistos",
    "applied-ai-engineering-lab": "applied-ai-engineering-lab",
    "sbst-vs-llm": "sbst-vs-llm",
    "album-copa-2026-local": "album-copa-2026-local",
}

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

class Document(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.refs: list[tuple[str, str, dict[str, str]]] = []
        self.lang = ""
        self.h1_count = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        if tag == "html":
            self.lang = values.get("lang", "")
        if tag == "h1":
            self.h1_count += 1
        if "id" in values:
            assert values["id"] not in self.ids, f"duplicate id: {values['id']}"
            self.ids.add(values["id"])
        for key in ("href", "src"):
            if key in values:
                self.refs.append((tag, values[key], values))
        if tag == "img":
            assert values.get("alt"), "image without alt"
            assert values.get("loading") == "lazy", "image without lazy loading"
            assert values.get("width") and values.get("height"), "image without dimensions"

docs: dict[Path, Document] = {}
for page in pages:
    content = page.read_text(encoding="utf-8")
    document = Document()
    document.feed(content)
    docs[page] = document
    assert document.h1_count == 1, f"expected one H1: {page}"
    assert document.lang == ("en" if page == pages[0] else "pt-BR"), f"wrong language: {page}"
    assert 'name="viewport"' in content, f"no viewport: {page}"
    assert "hreflang" in content, f"no language alternate: {page}"

checked = 0
for page, document in docs.items():
    for tag, raw, attrs in document.refs:
        parsed = urlsplit(raw)
        if parsed.scheme in ("https", "http"):
            assert parsed.scheme == "https", f"insecure link: {raw}"
            assert parsed.netloc in ("github.com", "www.linkedin.com", "insideairbnb.com", "ivanfborges.github.io"), f"unexpected host: {raw}"
            parts = parsed.path.strip("/").split("/")
            if parsed.netloc == "github.com" and len(parts) >= 5 and parts[0] == "ivanfborges" and parts[2] == "blob":
                folder = repo_folders.get(parts[1])
                assert folder, f"unknown source repo: {raw}"
                sibling = workspace / folder
                if sibling.is_dir():
                    assert (sibling / unquote("/".join(parts[4:]))).is_file(), f"missing report: {raw}"
            continue
        if parsed.scheme == "mailto":
            continue
        assert not parsed.scheme and not parsed.netloc, f"unexpected reference: {raw}"
        target = (page.parent / unquote(parsed.path)).resolve() if parsed.path else page
        assert target.is_relative_to(site), f"path outside site: {raw}"
        if target.is_dir():
            target /= "index.html"
        assert target.is_file(), f"missing local target: {raw}"
        if parsed.fragment:
            assert target in docs and parsed.fragment in docs[target].ids, f"missing fragment: {raw}"
        if tag == "img":
            data = target.read_bytes()
            assert data.startswith(b"\x89PNG\r\n\x1a\n"), f"unexpected image: {raw}"
            dimensions = struct.unpack(">II", data[16:24])
            assert dimensions == (int(attrs["width"]), int(attrs["height"])), f"wrong image dimensions: {raw}"
        checked += 1

airbnb = evidence["airbnb"]
topvistos = evidence["topvistos"]
assert sha(site / "assets" / "airbnb-training-map.png") == airbnb["training_map_sha256"]
assert sha(site / "assets" / "topvistos-final-evaluation.png") == topvistos["evaluation_chart_sha256"]
en = pages[0].read_text(encoding="utf-8")
pt = pages[1].read_text(encoding="utf-8")
assert f"BRL {airbnb['mae_brl']:.2f}" in en
assert f"BRL {airbnb['baseline_mae_brl']:.2f}" in en
assert f"R$ {airbnb['mae_brl']:.2f}".replace(".", ",") in pt
assert f"R$ {airbnb['baseline_mae_brl']:.2f}".replace(".", ",") in pt
reduction = (1 - airbnb["mae_brl"] / airbnb["baseline_mae_brl"]) * 100
assert f"{reduction:.2f}%" in en
assert f"{reduction:.2f}".replace(".", ",") + "%" in pt
assert str(topvistos["holdout_rows"]) in en.replace(",", "")
assert f"{topvistos['macro_f1']:.3f}" in en
assert f"{topvistos['macro_f1']:.3f}".replace(".", ",") in pt
for value in topvistos["macro_f1_95ci"]:
    assert f"{value:.3f}" in en
    assert f"{value:.3f}".replace(".", ",") in pt

verified_sources = 0
for record, folder, image_key, image_file in (
    (airbnb, "airbnb-rio", "training_map_path", "airbnb-training-map.png"),
    (topvistos, "kaggle-topvistos", "evaluation_chart_path", "topvistos-final-evaluation.png"),
):
    source = workspace / folder
    if source.is_dir():
        metrics = source / record["metrics_path"]
        image = source / record[image_key]
        assert sha(metrics) == record["metrics_sha256"], f"source metrics changed: {metrics}"
        assert sha(image) == sha(site / "assets" / image_file), f"source figure changed: {image}"
        verified_sources += 1

assert (site / ".nojekyll").is_file()
css = (site / "assets" / "site.css").read_text(encoding="utf-8")
assert "@media (max-width: 640px)" in css and "prefers-reduced-motion" in css
assert not re.search(r"<script\b", en + pt, re.I), "unexpected script"
print(f"PASS: {len(pages)} languages, {checked} local links/assets, 2 image hashes, metrics; {verified_sources} sibling sources")