# Ivan Borges — protótipo de site do portfólio

[English](README.md) · [Abrir página em português](pt/index.html) · [Open English page](index.html)

Protótipo local, ainda não publicado, para apresentar o trabalho de Ivan de forma breve e bilíngue. Ele acrescenta uma primeira leitura visual para recrutadores e líderes: dois estudos de caso mostram a pergunta, o resultado da avaliação e a principal limitação, com links para os repositórios técnicos. O perfil do GitHub continua como fonte de detalhes dos projetos.

O site usa apenas HTML e CSS. Não tem analytics, formulários, fontes externas, JavaScript, dependências de build, modelos binários ou dados privados. As duas figuras copiam saídas agregadas já públicas dos projetos. O arquivo [evidence.json](evidence.json) registra hashes e métricas agregadas publicadas. A figura do Airbnb credita o Inside Airbnb (CC BY 4.0).

## Visualizar e verificar

Nesta pasta:

~~~sh
python -m http.server 8000
~~~

Abra http://localhost:8000/ para inglês ou http://localhost:8000/pt/ para português. Para parar o servidor, pressione Ctrl+C.

~~~sh
python scripts/check_site.py
~~~

O verificador funciona em um checkout isolado. Se os repositórios Airbnb e TopVistos estiverem em pastas irmãs, compara também suas métricas públicas e os bytes das figuras com o manifesto. O site usa apenas os próprios arquivos e links para os relatórios originais.

## Decisão de publicação

Nenhum repositório GitHub, deploy no GitHub Pages, domínio ou serviço pago foi criado para este protótipo. Se Ivan decidir publicá-lo, um repositório público chamado `ivanfborges.github.io` oferece um endereço padrão sem compra de domínio. O [guia oficial do GitHub Pages](https://docs.github.com/en/pages/quickstart) documenta esse caminho. Um domínio próprio é opcional e exigiria decisão separada.

Antes de publicar, Ivan deve revisar a apresentação em primeira pessoa, os fatos profissionais, o tom visual e se um site separado ajuda nas candidaturas. Se algum resultado de origem mudar, atualizar juntas as páginas nos dois idiomas e o manifesto de evidências. Não alterar silenciosamente os resultados congelados do Kaggle ou Airbnb.