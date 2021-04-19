# brazil-finances

## Motivo

Este projeto surgiu após verificar a dificuldade de acesso a informações relacionadas
ao mercado financeiro brasileiro, onde apenas projetos com grande investimento
são capazes de consumir dados de qualidade provenientes de empresas privadas.

O acesso a essas informações, as quais consistem em sua maioria de dados públicos,
deveria ser algo simples e de fácil acesso, o que favoreceria o desenvolvimento de novas
iniciativas.

Logo, este projeto, sendo iniciado de forma experimental e ainda em desenvolvimento,
tem como objetivo facilitar o acesso aos dados do sistema financeiro brasileiro, tais como
demonstrativos de resultados de empresas listadas na bolsa, indicadores fundamentalistas,
informes e periódicos, e quem sabe futuramente cotações de ativos.

O intuito é consumir grande parte dos dados fornecidos pela CVM e B3 para criar
serviços com endpoints mais modernos e dados 'utilizáveis' por desenvolvedores e afins.

## Contribuição

Este projeto está em seu início ainda, portanto colaboradores e interessados são
extremamente bem-vindos.

## Instalação

```
pipenv install
```

```
pipenv shell
```

## Dados

Ao executar os notebooks presentes em `notebooks` serão criadas as pastas cmv e b3 na pasta
`data`, nessas pastas serão salvos os arquivos processados a partir dos downloads dos
arquivos obtidos nos sites da B3 e da CVM.

Infelizmente, alguns dados provenientes da B3 devem ser baixados manualmente, devido a necessidade de informar captcha.
Os arquivos devem ser baixados
[aqui](http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/mercado-a-vista/series-historicas/)
e salvos por padrão em `data/b3/cotacoes_historicas/download/`,
para mais detalhes ou para alterar o caminho a ser salvo, verificar o caderno `notebooks/cotacoes_historicas_b3.ipynb`.

Para mais detalhes, consultar os scripts da pasta `notebooks`.

## Termos de uso

Iniciativa feita de brasileiros para brasileiros, sinta-se a vontade para utilizar
e contribuir com esse projeto.
