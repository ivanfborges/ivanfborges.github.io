# Ivan Borges — site do portfólio

[English](README.md) · [Visitar o site](https://ivanfborges.github.io/pt/) · [English website](https://ivanfborges.github.io/)

Apresentação breve e bilíngue do trabalho de Ivan. Dois estudos de caso visuais mostram a pergunta, o resultado da avaliação e a principal limitação, com links para os repositórios técnicos. O perfil GitHub continua como fonte de detalhes dos projetos.

O site usa apenas HTML e CSS, publicado pelo GitHub Pages a partir da raiz da branch main. Não tem analytics, formulários, fontes externas, JavaScript, dependências de build, modelos binários ou dados privados. As duas figuras copiam saídas agregadas já públicas dos projetos. O arquivo [evidence.json](evidence.json) registra hashes e métricas agregadas publicadas. A figura do Airbnb credita o Inside Airbnb (CC BY 4.0).

## Visualizar e verificar localmente

Nesta pasta:

~~~sh
python -m http.server 8000
~~~

Abra http://localhost:8000/ para inglês ou http://localhost:8000/pt/ para português. Pare o servidor com Ctrl+C.

~~~sh
python scripts/check_site.py
~~~

O verificador funciona em um checkout isolado. Se os repositórios Airbnb e TopVistos estiverem em pastas irmãs, compara também suas métricas públicas e os bytes das figuras com o manifesto. Se um resultado de origem mudar, atualize juntas as páginas nos dois idiomas e o manifesto de evidências. Não altere silenciosamente os resultados congelados do Kaggle ou Airbnb.

O domínio padrão do GitHub Pages não exige compra de domínio. Os detalhes da publicação estão na [documentação do GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).