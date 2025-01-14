import streamlit as st
import pandas as pd

# Carregar arquivo
arquivo = '(nome do arquivo)'
arquivo = pd.read_excel(arquivo)

# Tabela de visualização
st.title("Dados do arquivo")
st.dataframe(arquivo)

# Exibir duplicatas
duplicatas = arquivo[arquivo.duplicated()]
st.write(f"Total de duplicatas: {len(duplicatas)}")
st.dataframe(duplicatas)

# Dados limpos
df_limpo = arquivo.drop_duplicates()
st.write("Dados após limpeza:")
st.dataframe(df_limpo)

# Gráfico
st.write("Campos com valores nulos:")
st.bar_chart(df_limpo.isnull().sum())


# para rodar o código e visualizar as tabelas,utilizar "Streamlit run (nome_arquivo.py) no terminal"
