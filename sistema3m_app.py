import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

st.set_page_config(page_title="Simulador 3M - Aluno", layout="wide")

st.title("📊 Simulador 3M - Sistema do Aluno")

# Etapa 1 - Cadastro do fundo
with st.expander("1️⃣ Cadastro do Fundo"):
    nome_fundo = st.text_input("Nome do Fundo:")
    patrimonio = st.number_input("Patrimônio Inicial (R$):", min_value=0.0, step=100.0)
    membros = st.text_area("Membros (separar por vírgula):")

    if nome_fundo and patrimonio > 0 and membros:
        st.success("✅ Fundo cadastrado com sucesso!")

# Etapa 2 - Download de templates
with st.expander("2️⃣ Baixar Modelos de Planilhas"):
    with open("data/template_dre.xlsx", "rb") as f:
        st.download_button("⬇️ Baixar Planilha DRE", f, file_name="template_dre.xlsx")

    with open("data/template_indicadores.xlsx", "rb") as f:
        st.download_button("⬇️ Baixar Planilha de Indicadores", f, file_name="template_indicadores.xlsx")

# Etapa 3 - Upload da DRE preenchida
with st.expander("3️⃣ Enviar Planilha DRE preenchida"):
    arquivo_dre = st.file_uploader("📎 Envie o arquivo DRE (.xlsx)", type=["xlsx"])
    if arquivo_dre:
        df_dre = pd.read_excel(arquivo_dre)
        st.dataframe(df_dre)
        st.success("✅ DRE enviada com sucesso!")

# Etapa 4 - Upload da planilha de indicadores
with st.expander("4️⃣ Enviar Indicadores preenchidos"):
    arquivo_ind = st.file_uploader("📎 Envie o arquivo de Indicadores (.xlsx)", type=["xlsx"])
    if arquivo_ind:
        df_ind = pd.read_excel(arquivo_ind)
        st.dataframe(df_ind)
        st.success("✅ Indicadores enviados com sucesso!")
