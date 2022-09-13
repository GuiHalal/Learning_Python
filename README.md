# Learning_Python

Repositório para guardar os exercícios que fiz durante os cursos de Python da Alura.

## Sumário

- [Curso de Python para Data Science: linguagem e Numpy](#curso-de-python-para-data-science-linguagem-e-numpy-)
- [ Python Pandas: tratando e analisando dados](#python-pandas-tratando-e-analisando-dados)

1. ## [Python: começando com a linguagem](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#python-come%C3%A7ando-com-a-linguagem)
   1.  [Instalação do Python 3 ](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md)
   2.  [Lidando com a entrada do usuário](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#2---lidando-com-a-entrada-do-usu%C3%A1rio)
   3.  [Testando valores](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#3---testando-valores)
   4.  [A sequência do jogo](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#4---a-sequ%C3%AAncia-do-jogo)
   5.  [Iterando de maneira diferente](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#5---iterando-de-maneira-diferente)
   6.  [Gerando números aleatórios](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#6---gerando-n%C3%BAmeros-aleat%C3%B3rios)
   7.  [Nível e Pontuação](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#7---n%C3%ADvel-e-pontua%C3%A7%C3%A3o)
   8.  [Organizando ainda melhor o nosso código](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#8--organizando-ainda-melhor-o-nosso-c%C3%B3digo)
   9.  [Comparando `Python` com `C`](https://github.com/GuiHalal/Learning_Python/blob/main/Python:%20come%C3%A7ando%20com%20a%20linguagem/jogos/Conte%C3%BAdo.md#9---comparando-python-com-c)
## Curso de Python para Data Science: linguagem e Numpy

#### 1 - Ambiente do cientista de dados

- Os ambientes de desenvolvimento para a linguagem Python
- A carregar dados externos em arrays Numpy
- A trabalhar de forma básica com arrays Numpy

#### 2 - Características do Python

- A realizar operações matemáticas com Python
- Como criar e atribuir valores a variáveis na linguagem Python
- Os tipos de dados básicos em Python
- A realizar transformações de tipos de dados
- As regras e características básicas da linguagem Python (indentação, comentários e interpolação de strings)

#### 3 - Trabalhando com listas

- Listas, que são um tipo de sequência mutável que podemos utilizar para armazenar coleções de itens
- Formas de criação de listas em Python
- A realizar operações básicas com listas, como a pertinência, concatenação e verificação de características
- Técnicas de seleção de itens e fatiamento com listas do Python
- A utilizar métodos básicos de listas

#### 4 - Condicionais e laços

- Como utilizar estruturas de repetição e condicionais na linguagem Python
- A construção de laços for
- A iteração em listas do Python
- Loops aninhados em listas de listas
- Cláusulas if, elif e else
- Operadores lógicos e de comparação
- List comprehensions

#### 5 - Conhecendo o NumPy

- A importação de pacotes em Python
- Técnicas para criação de arrays Numpy
- Arrays de mais de uma dimensão
- Comparações de desempenho entre arrays Numpy e listas do Python
- Operações aritméticas com arrays Numpy
- Seleções de itens e fatiamentos em arrays
- Indexação com arrays booleanos
- Atributos e métodos de arrays no pacote Numpy
- A geração de estatísticas descritivas e sumarizações com arrays

## Python Pandas: tratando e analisando dados

#### 1 - Conhecendo Jupyter

- **Anaconda** é a principal distribuição para cientistas de dados que usam Python
- **Jupyter** é a nossa ferramenta para executar código Python e visualizar os dados
- **Ambientes virtuais** ajudam a isolar um projeto para definir a versão das bibliotecas e do próprio Python

#### 2 - Importando dados

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

#### 3 - Series e Index

- Como selecionar uma variável do dataframe (por exemplo, `dados['Tipo']` ou `dados.Tipo`)
- Que um dataframe é composto de vários `Series`
- Como eliminar duplicatas (pelo método `drop_duplicates()`)
- Como redefinir o index de um dataframe e series (atributo `index`)
- Como concatenar dataframes (lembrando do `axis`)
- Como criar novos dataframes baseados em estruturas de dados Python (lista, dicionários ou tuples)

#### 4 - Filtrando dados

- Criar uma Series booleana usando o método `isin(..)` a partir do dataframe
- Filtrar os dados de um dataframe baseado na Series booleana
- Exportar e gravar os dados do dataframe (método `to_csv()`)
- Ordenar os dados de um dataframe (métodos `sort_values()` e `sort_index()`)

#### 5 - Frequências de imóveis

- Formas de seleção e frequências
- Seleção com a condição OR (`|`)
- Seleção com a condição AND (`&`)
- Como criar um `Index` com `split()`
- Seleção por linha e coluna em um dataframe:
  - Utilizando os índices numéricos e os rótulos das linhas

#### 6 - Tratamento de dados faltantes

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

#### 7 - Novas variáveis

- Como criar variáveis
- Como excluir variáveis utilizando `del`, `pop()` e `drop()`
- Contadores, através do `value_counts()`

#### 8 - Estatística Descritiva

- Como criar agrupamentos com o `groupby()`
- Estatísticas descritivas com o` describe()` e o `aggregate()`
- Como renomear as colunas com o `rename()`
- Como fazer gráficos com o pacote **Matplotlib**
- Como criar faixas de valor com o `cut()`

#### 9 - Removendo Outliers

- Como identificar e remover outliers com o box plot
- Como fazer um gráfico de pizza com a aplicação do método `pie()`, da biblioteca `matplotlib`
