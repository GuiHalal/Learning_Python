# Learning_Python

Repositório para guardar os exercícios que fiz durante os cursos de Python da Alura.

## Python: começando com a linguagem

### O que aprendemos?

#### 1 - Instalação do Python 3

- Apresentação
- Instalando o Python no Windows
- Instalando em outras plataformas
- Usar o Python sem instalá-lo
- Função print e variáveis
- Imprimindo uma mensagem na tela
- Personalizando a saída
- Imprimindo datas
- Tipagem do Python
- Tipagem de variáveis

#### 2 - Lidando com a entrada do usuário

- Instalando e conhecendo o PyCharm
- Mão na massa: Primeiro projeto com PyCharm
- Comparando variáveis
- Impossível acertar o número
- Python 2 vs Python 3
- Para saber mais: JavaScript vs Python

#### 3 - Testando valores

- A condição elif
- Faixa Etária
- Faixa Etária - Variáveis
- If..else. e nada funciona!
- Mão na massa: Dando dicas
- Qual é o tipo?
- Para saber mais: if sem ou com parênteses?

#### 4 - A sequência do jogo

- O laço com while
- Resultado do programa
- if e while
- Formatação de strings
- Testando formatação
- Mão na massa: Usando while
  
#### 5 - Iterando de maneira diferente

- O laço com for
- De while para for
- Encerrando a interação e o loop
- break e continue
- while com break
- for com continue
- Mão na massa: Usando for
- Para saber mais: Formatação de strings
- Adaptando o Padrão Americano
- O resultado da interpolação
- Interpolação - Python 2 vs Python 3

#### 6 - Gerando números aleatórios

- Gerando e arredondando um número aleatório
- Importar módulo
- Definindo um intervalo para a geração de números aleatórios
- O menor e o maior
- Múltiplos aleatórios
- O grande sorteio
- Mão na massa: Número secreto aleatório
- Para saber mais: Pseudo-Random

#### 7 - Nível e Pontuação

- Adicionando níveis ao jogo
- Definindo uma pontuação para o usuário
- Funções built-in
- Dividindo pontos
- Mão na massa: Níveis e Pontuação
- Para saber mais: arredondar no Python 2 e no Python 3
- Para saber mais: Divisão de float e integer

#### 8 -Organizando ainda melhor o nosso código

- Importando arquivos dentro de outros
- Criando funções para os nossos jogos
- Declarando funções
- Importação de módulo
- Importação de módulo, mas um pouco diferente
- Diferenciando um arquivo executado de um importado
- Um módulo pode se chamar automaticamente?
- Mão na massa: Modularizando o jogo

#### 9 - Comparando Python com C

- Python vs C
- Interpretado vs Compilado
- Python é interpretado ou compilado?

## Curso de Python para Data Science: linguagem e Numpy

### O que aprendemos?

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

### O que aprendemos?

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
- Como excluir variáveis utilizando` del`,` pop()` e `drop()`
- Contadores, através do `value_counts()`