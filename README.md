# Ivan Borges — portfolio site

[Português](README.pt-BR.md) · [Visit the site](https://ivanfborges.github.io/) · [Versão em português](https://ivanfborges.github.io/pt/)

A concise bilingual introduction to Ivan's work. Two visual case studies show the question, evaluation result and main limitation, then link to the technical repositories. The GitHub profile remains the source of deeper project detail.

The site is plain HTML and CSS, published from the root of the main branch with GitHub Pages. It has no analytics, forms, external fonts, JavaScript, build dependencies, model binaries or private data. The two figures are copies of already public, aggregate project outputs. [evidence.json](evidence.json) records their hashes and the published aggregate metrics. The Airbnb figure credits Inside Airbnb (CC BY 4.0).

## Preview and verify locally

From this directory:

~~~sh
python -m http.server 8000
~~~

Open http://localhost:8000/ for English or http://localhost:8000/pt/ for Portuguese. Stop the server with Ctrl+C.

~~~sh
python scripts/check_site.py
~~~

The checker works in a standalone checkout. When the Airbnb and TopVistos repositories are sibling directories, it additionally compares their public metrics and figure bytes with the manifest. When a source result changes, update both language pages and the evidence manifest together. Do not silently update frozen Kaggle or Airbnb results.

The default GitHub Pages domain needs no purchased domain. Deployment details are in the [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).