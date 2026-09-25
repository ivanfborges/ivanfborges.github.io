# Ivan Borges — portfolio site prototype

[Português](README.pt-BR.md) · [Open English page](index.html) · [Abrir página em português](pt/index.html)

A local, unpublished prototype for a concise bilingual introduction to Ivan's work. It adds a visual first pass for recruiters and leaders: two short case studies show the question, evaluation result and main limitation, then link to the technical repositories. The GitHub profile remains the source of deeper project detail.

The site is plain HTML and CSS. It has no analytics, forms, external fonts, JavaScript, build dependencies, model binaries or private data. The two figures are copies of already public, aggregate project outputs. [evidence.json](evidence.json) records their hashes and the published aggregate metrics. The Airbnb figure credits Inside Airbnb (CC BY 4.0).

## Preview and verify

From this directory:

~~~sh
python -m http.server 8000
~~~

Open http://localhost:8000/ for English or http://localhost:8000/pt/ for Portuguese. To stop the server, press Ctrl+C.

~~~sh
python scripts/check_site.py
~~~

The checker works in a standalone checkout. When the Airbnb and TopVistos repositories are sibling directories, it additionally compares their public metrics and figure bytes with the manifest. The site itself uses only its own files and links to the original reports.

## Publication decision

No GitHub repository, GitHub Pages deployment, domain or paid service has been created for this prototype. If Ivan chooses to publish it, a public repository named `ivanfborges.github.io` would provide a default URL without buying a domain. The [GitHub Pages quickstart](https://docs.github.com/en/pages/quickstart) documents this route. A custom domain is optional and would require a separate decision.

Before publication, Ivan should review the first-person introduction, professional facts, visual tone and whether a separate site is useful in applications. When a source result changes, update both language pages and the evidence manifest together. Do not silently update frozen Kaggle or Airbnb results.