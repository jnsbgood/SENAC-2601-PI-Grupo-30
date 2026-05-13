# etl.py
import pandas as pd

def carregar_dados(caminho):
    """Carrega a base original e realiza transformações iniciais."""
    df = pd.read_csv(caminho)
    
    # Exemplo de limpeza e criação de variável derivada
    df["Income_to_CreditRatio"] = df["Income"] / df["Credit_Limit"]
    
    # Remover colunas irrelevantes
    df.drop(columns=["Unnamed: 0"], errors="ignore", inplace=True)
    
    # Salvar base tratada
    df.to_csv("dados/base_tratada.csv", index=False)
    print("Base tratada salva com sucesso!")

if __name__ == "__main__":
    carregar_dados("dados/base_original.csv")

