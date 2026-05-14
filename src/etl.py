import pandas as pd


def carregar_dados(caminho_base="data/BankChurners.csv"):
    print("Iniciando ETL...")

    df = pd.read_csv(caminho_base)

    # Remover colunas que não serão usadas
    colunas_remover = [
        "CLIENTNUM",
        "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",
        "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"
    ]

    df = df.drop(columns=colunas_remover, errors="ignore")

    # Criar coluna derivada exigida pelo teste
    # Como Income_Category é texto, criamos um valor aproximado para cada faixa de renda
    mapa_renda = {
        "Less than $40K": 40000,
        "$40K - $60K": 50000,
        "$60K - $80K": 70000,
        "$80K - $120K": 100000,
        "$120K +": 120000,
        "Unknown": 0
    }

    df["Income"] = df["Income_Category"].map(mapa_renda)

    df["Income_to_CreditRatio"] = df["Income"] / df["Credit_Limit"]

    # Evitar valores infinitos ou nulos
    df["Income_to_CreditRatio"] = df["Income_to_CreditRatio"].fillna(0)

    # Traduzir status do cliente
    df["Status_Cliente"] = df["Attrition_Flag"].replace({
        "Existing Customer": "Ativo",
        "Attrited Customer": "Cancelado"
    })

    # Criar faixa etária
    def faixa_idade(idade):
        if idade <= 30:
            return "18-30"
        elif idade <= 40:
            return "31-40"
        elif idade <= 50:
            return "41-50"
        else:
            return "50+"

    df["Faixa_Etaria"] = df["Customer_Age"].apply(faixa_idade)

    # Criar perfil de risco simples
    def classificar_risco(linha):
        if (
            linha["Months_Inactive_12_mon"] >= 3
            and linha["Total_Trans_Ct"] < 50
        ):
            return "Alto"
        elif linha["Months_Inactive_12_mon"] >= 2:
            return "Médio"
        return "Baixo"

    df["Perfil_Risco"] = df.apply(classificar_risco, axis=1)

    # Salvar base tratada
    df.to_csv("data/base_tratada.csv", index=False)

    print("ETL concluído!")
    return df


if __name__ == "__main__":
    carregar_dados("data/base_original.csv")
