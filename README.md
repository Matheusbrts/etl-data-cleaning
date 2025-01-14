# ETL inical com Python

Este projeto realiza a limpeza de dados em arquivos CSV ou Excel, removendo as duplicatas e substituindo valores nulos por uma string de erro. O arquivo limpo é então salvo como um arquivo CSV.

## Funcionalidades

- **Carregar o  Arquivo**: Suporta arquivos `.csv` e `.xlsx`.
- **Verificar e Remover Duplicatas**: Remove duplicatas do arquivo e salva os registros duplicados em um arquivo `duplicatas.csv`.
- **Preencher Valores Nulos**: Substitui valores nulos por `#Error#`.
- **Salvar Arquivo Limpo**: Salva o DataFrame limpo em um novo arquivo CSV.

## Tecnologias e Bibliotecas

Este projeto usa as seguintes bibliotecas:

- `pandas`: Para manipulação de dados.
- `numpy`: Para operações numéricas.
- `colorama`: Para adicionar cores às mensagens no terminal.

### Requisitos

- Python 3.6 ou superior.
- Sistema operacional: Windows, Linux ou macOS.
- Pode ser utilizado também em um ambiente virtual

### Instalação
