import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns



# Configuração da página

st.set_page_config(

    page_title="Dashboard Credit Card Churn",

    layout="wide"

)



# Título

st.title("📊 Dashboard - Credit Card Customers")

st.write(

    "Análise do perfil dos clientes propensos ao cancelamento do cartão de crédito."

)



# Carregar base

df = pd.read_csv("data/base_tratada.csv")



# ----------------------------

# FILTROS

# ----------------------------



st.sidebar.header("Filtros")



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



# Filtrar dados

df_filtrado = df[

    (df["Gender"].isin(genero)) &

    (df["Status_Cliente"].isin(status)) &

    (df["Perfil_Risco"].isin(risco))

]



# ----------------------------

# KPIs

# ----------------------------



st.subheader("Indicadores Gerais")



col1, col2, col3, col4 = st.columns(4)



total_clientes = len(df_filtrado)



clientes_cancelados = len(

    df_filtrado[

        df_filtrado["Status_Cliente"] == "Cancelado"

    ]

)



taxa_cancelamento = (

    clientes_cancelados / total_clientes * 100

    if total_clientes > 0 else 0

)



idade_media = (

    df_filtrado["Customer_Age"].mean()

)



col1.metric(

    "Total de Clientes",

    total_clientes

)



col2.metric(

    "Clientes Cancelados",

    clientes_cancelados

)



col3.metric(

    "Taxa de Cancelamento",

    f"{taxa_cancelamento:.2f}%"

)



col4.metric(

    "Idade Média",

    f"{idade_media:.0f} anos"

)



st.divider()



# ----------------------------

# GRÁFICOS

# ----------------------------



col_esq, col_dir = st.columns(2)



# gráfico 1

with col_esq:

    st.subheader("Clientes Ativos vs Cancelados")



    fig1, ax1 = plt.subplots()



    sns.countplot(

        x="Status_Cliente",

        data=df_filtrado,

        ax=ax1

    )



    st.pyplot(fig1)



# gráfico 2

with col_dir:

    st.subheader("Perfil de Risco")



    fig2, ax2 = plt.subplots()



    sns.countplot(

        x="Perfil_Risco",

        data=df_filtrado,

        ax=ax2

    )



    st.pyplot(fig2)



# gráfico 3

st.subheader("Cancelamento por Faixa Etária")



fig3, ax3 = plt.subplots(figsize=(8,4))



cancelados = df_filtrado[

    df_filtrado["Status_Cliente"] == "Cancelado"

]



sns.countplot(

    x="Faixa_Etaria",

    data=cancelados,

    ax=ax3

)



st.pyplot(fig3)



# gráfico 4

st.subheader("Cancelamento por Gênero")



fig4, ax4 = plt.subplots()



sns.countplot(

    x="Gender",

    hue="Status_Cliente",

    data=df_filtrado,

    ax=ax4

)



st.pyplot(fig4)



# ----------------------------

# TABELA

# ----------------------------



st.subheader("Tabela de Clientes")



st.dataframe(df_filtrado)

JANINY ANDRADE DA NOBREGA
20:10
import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns



# Configuração da página

st.set_page_config(

    page_title="Dashboard Credit Card Churn",

    layout="wide"

)



# Título

st.title("📊 Dashboard - Credit Card Customers")

st.write(

    "Análise do perfil dos clientes propensos ao cancelamento do cartão de crédito."

)



# Carregar base

df = pd.read_csv("data/base_tratada.csv")



# ----------------------------

# FILTROS

# ----------------------------



st.sidebar.header("Filtros")



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



# Filtrar dados

df_filtrado = df[

    (df["Gender"].isin(genero)) &

    (df["Status_Cliente"].isin(status)) &

    (df["Perfil_Risco"].isin(risco))

]



# ----------------------------

# KPIs

# ----------------------------



st.subheader("Indicadores Gerais")



col1, col2, col3, col4 = st.columns(4)



total_clientes = len(df_filtrado)



clientes_cancelados = len(

    df_filtrado[

        df_filtrado["Status_Cliente"] == "Cancelado"

    ]

)



taxa_cancelamento = (

    clientes_cancelados / total_clientes * 100

    if total_clientes > 0 else 0

)



idade_media = (

    df_filtrado["Customer_Age"].mean()

)



col1.metric(

    "Total de Clientes",

    total_clientes

)



col2.metric(

    "Clientes Cancelados",

    clientes_cancelados

)



col3.metric(

    "Taxa de Cancelamento",

    f"{taxa_cancelamento:.2f}%"

)



col4.metric(

    "Idade Média",

    f"{idade_media:.0f} anos"

)



st.divider()



# ----------------------------

# GRÁFICOS

# ----------------------------



col_esq, col_dir = st.columns(2)



# gráfico 1

with col_esq:

    st.subheader("Clientes Ativos vs Cancelados")



    fig1, ax1 = plt.subplots()



    sns.countplot(

        x="Status_Cliente",

        data=df_filtrado,

        ax=ax1

    )



    st.pyplot(fig1)



# gráfico 2

with col_dir:

    st.subheader("Perfil de Risco")



    fig2, ax2 = plt.subplots()



    sns.countplot(

        x="Perfil_Risco",

        data=df_filtrado,

        ax=ax2

    )



    st.pyplot(fig2)



# gráfico 3

st.subheader("Cancelamento por Faixa Etária")



fig3, ax3 = plt.subplots(figsize=(8,4))



cancelados = df_filtrado[

    df_filtrado["Status_Cliente"] == "Cancelado"

]



sns.countplot(

    x="Faixa_Etaria",

    data=cancelados,

    ax=ax3

)



st.pyplot(fig3)



# gráfico 4

st.subheader("Cancelamento por Gênero")



fig4, ax4 = plt.subplots()



sns.countplot(

    x="Gender",

    hue="Status_Cliente",

    data=df_filtrado,

    ax=ax4

)



st.pyplot(fig4)



# ----------------------------

# TABELA

# ----------------------------



st.subheader("Tabela de Clientes")
st.dataframe(df_filtrado)

JANINY ANDRADE DA NOBREGA
20:24
# ----------------------------

# CONCLUSÃO AUTOMÁTICA

# ----------------------------



st.subheader("📌 Estratégia de Retenção")



st.info(

    """

    Clientes classificados como **Alto Risco**

    devem receber ações preventivas, como:

    

    - contato do gerente;

    - benefícios no cartão;

    - renegociação de taxas;

    - campanhas de fidelização.

    """

)
