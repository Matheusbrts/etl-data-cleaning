# ETL inical de arquivos XLSX E CSV

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

#Como usar

1 . Execute o script no terminal:

    python (nome_script).py

2. O programa vai solicitar que você forneça o caminho do arquivo que deseja limpar, desde que seja .csv ou .xlsx.

   **Exemplo de entrada : Entre com o nome do arquivo (ou caminho completo): dados.csv**

3. Será realizada as etapas automaticamente:

  * Carregamento do arquivo de dados.
    
  * Verificação e remoção de duplicatas (se houver).
  
  * Substituição de valores nulos por #Error#.
  
  * Salvamento do arquivo limpo como Limp_arquivo.csv.
  
  * Se duplicatas forem encontradas, elas vão ser salvas em um arquivo chamado duplicatas.csv.


4. Ao final, o programa exibirá uma mensagem indicando o sucesso do script rodado e o nome do arquivo gerado.

---
**Exemplo de Execução:**

Olá, seja bem-vindo! Vamos limpar seus dados?

Entre com o nome do arquivo (ou caminho completo): dados.csv

Aguarde por 2 segundos, verificando arquivos...

Carregando arquivo CSV...

Totais de linhas: 100, Totais de colunas: 5

Total de duplicatas encontradas: 3

Duplicatas removidas e salvas em 'duplicatas.csv'.

Total de valores nulos encontrados: 10

Todos os valores nulos foram preenchidos com '#Error#'!

Dados limpos com sucesso! Total de linhas: 97, Total de colunas: 5

Arquivo limpo salvo como Limp_arquivo.csv.

---

**Arquivos Gerados**:

Limp_arquivo.csv: Este arquivo contém os dados limpos, com duplicatas removidas e valores nulos substituídos por #Error#.

duplicatas.csv: Caso exista duplicatas no arquivo original, elas serão salvas nesse arquivo.








