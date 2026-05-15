import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração da página
st.set_page_config(
    page_title="Dashboard Credit Card Churn",
    layout="wide"
)

# Título Principal
st.title("📊 Dashboard - Credit Card Customers")
st.write("Análise do perfil dos clientes propensos ao cancelamento do cartão de crédito.")

# Carregar base de dados
# Certifique-se de que o arquivo base_tratada.csv existe na pasta data
try:
    df = pd.read_csv("data/base_tratada.csv")
except FileNotFoundError:
    st.error("Erro: O arquivo 'data/base_tratada.csv' não foi encontrado. Rode o script de ETL primeiro.")
    st.stop()

# ----------------------------
# FILTROS NA BARRA LATERAL
# ----------------------------
st.sidebar.header("Filtros de Pesquisa")

genero = st.sidebar.multiselect(
    "Gênero",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

status = st.sidebar.multiselect(
    "Status do Cliente",
    options=df["Status_Cliente"].unique(),
    default=df["Status_Cliente"].unique()
)

risco = st.sidebar.multiselect(
    "Perfil de Risco",
    options=df["Perfil_Risco"].unique(),
    default=df["Perfil_Risco"].unique()
)

# Aplicando os filtros nos dados
df_filtrado = df[
    (df["Gender"].isin(genero)) &
    (df["Status_Cliente"].isin(status)) &
    (df["Perfil_Risco"].isin(risco))
]

# ----------------------------
# INDICADORES (KPIs)
# ----------------------------
st.subheader("Principais Indicadores")
col1, col2, col3, col4 = st.columns(4)

total_clientes = len(df_filtrado)
clientes_cancelados = len(df_filtrado[df_filtrado["Status_Cliente"] == "Cancelado"])
taxa_cancelamento = (clientes_cancelados / total_clientes * 100 if total_clientes > 0 else 0)
idade_media = df_filtrado["Customer_Age"].mean()

col1.metric("Total de Clientes", total_clientes)
col2.metric("Clientes Cancelados", clientes_cancelados)
col3.metric("Taxa de Churn", f"{taxa_cancelamento:.2f}%")
col4.metric("Idade Média", f"{idade_media:.0f} anos")

st.divider()

# ----------------------------
# VISUALIZAÇÕES GRÁFICAS
# ----------------------------
col_esq, col_dir = st.columns(2)

with col_esq:
    st.subheader("Distribuição de Status")
    fig1, ax1 = plt.subplots()
    sns.countplot(x="Status_Cliente", data=df_filtrado, ax=ax1, palette="viridis")
    st.pyplot(fig1)

with col_dir:
    st.subheader("Análise de Perfil de Risco")
    fig2, ax2 = plt.subplots()
    sns.countplot(x="Perfil_Risco", data=df_filtrado, ax=ax2, palette="magma")
    st.pyplot(fig2)

st.subheader("Cancelamentos por Faixa Etária")
fig3, ax3 = plt.subplots(figsize=(10, 4))
cancelados = df_filtrado[df_filtrado["Status_Cliente"] == "Cancelado"]
if not cancelados.empty:
    sns.countplot(x="Faixa_Etaria", data=cancelados, ax=ax3, order=sorted(df["Faixa_Etaria"].unique()))
    st.pyplot(fig3)
else:
    st.write("Nenhum cliente cancelado nos filtros selecionados.")

# ----------------------------
# TABELA DE DADOS E CONCLUSÃO
# ----------------------------
st.subheader("Dados Detalhados")
st.dataframe(df_filtrado, use_container_width=True)

st.info("""
    **💡 Sugestão Estratégica:**
    Clientes em áreas de 'Alto Risco' devem ser priorizados com campanhas de retenção e benefícios exclusivos.
    """)
