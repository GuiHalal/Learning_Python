# Python Pandas: tratando e analisando dados

## 1 - Conhecendo Jupyter

- **Anaconda** é a principal distribuição para cientistas de dados que usam Python
- **Jupyter** é a nossa ferramenta para executar código Python e visualizar os dados
- **Ambientes virtuais** ajudam a isolar um projeto para definir a versão das bibliotecas e do próprio Python

## 2 - Importando dados

- Como importar a biblioteca (import pandas as pd)
- Como ler fontes de dados diferentes
  - Uma base CSV (`pd.read_csv(...)`)
  - Uma base JSON (`pd.read_json(...)`)
  - Uma base TXT (`pd.read_table(...)`)
  - Um arquivo EXCEL (`pd.read_excel(...)`)
  - Uma página HTML (`pd.read_html(...)`)
- Vários métodos e atributos úteis de dataframes, como:
  - `info()`
  - `head()`
  - `dtypes`
  - `columns`
  - `shape`
- Criar diferentes tipos de células dentro do Jupyter
- Acessar a documentação no Jupyter
- Como reexecutar todas as células no Jupyter

## 3 - Series e Index

- Como selecionar uma variável do dataframe (por exemplo, `dados['Tipo']` ou `dados.Tipo`)
- Que um dataframe é composto de vários `Series`
- Como eliminar duplicatas (pelo método `drop_duplicates()`)
- Como redefinir o index de um dataframe e series (atributo `index`)
- Como concatenar dataframes (lembrando do `axis`)
- Como criar novos dataframes baseados em estruturas de dados Python (lista, dicionários ou tuples)

## 4 - Filtrando dados

- Criar uma Series booleana usando o método `isin(..)` a partir do dataframe
- Filtrar os dados de um dataframe baseado na Series booleana
- Exportar e gravar os dados do dataframe (método `to_csv()`)
- Ordenar os dados de um dataframe (métodos `sort_values()` e `sort_index()`)

## 5 - Frequências de imóveis

- Formas de seleção e frequências
- Seleção com a condição OR (`|`)
- Seleção com a condição AND (`&`)
- Como criar um `Index` com `split()`
- Seleção por linha e coluna em um dataframe:
  - Utilizando os índices numéricos e os rótulos das linhas

## 6 - Tratamento de dados faltantes

- Tratamento de dados faltantes
- Como identificar valores nulos (missing values)
  - O método `isnull()` indica se os valores são nulos
  - O método `notnull()` retorna o contrário do método `isnull()`
  - O método `info()` também é uma forma de se verificar a presença de valores faltantes
- Como remover valores nulos com o método dropna()
- Tratamento condicional
- Inversão de valores booleanos com `~`
- Como substituir os missing values com o método fillna()
- Métodos de interpolação: `ffill`, `bfill` e `mean()`

## 7 - Novas variáveis

- Como criar variáveis
- Como excluir variáveis utilizando `del`, `pop()` e `drop()`
- Contadores, através do `value_counts()`

## 8 - Estatística Descritiva

- Como criar agrupamentos com o `groupby()`
- Estatísticas descritivas com o` describe()` e o `aggregate()`
- Como renomear as colunas com o `rename()`
- Como fazer gráficos com o pacote **Matplotlib**
- Como criar faixas de valor com o `cut()`

## 9 - Removendo Outliers

- Como identificar e remover outliers com o box plot
- Como fazer um gráfico de pizza com a aplicação do método `pie()`, da biblioteca `matplotlib`
