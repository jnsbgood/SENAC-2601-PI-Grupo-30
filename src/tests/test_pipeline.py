# test_pipeline.py
import os
import pandas as pd
import pytest
from src import etl, modelo

def test_etl_cria_base_tratada(tmp_path):
    # Executa ETL
    caminho_base = "data/base_original.csv"
    etl.carregar_dados(caminho_base)

    # Verifica se arquivo tratado foi criado
    assert os.path.exists("data/base_tratada.csv")

    # Verifica se contém coluna derivada
    df = pd.read_csv("data/base_tratada.csv")
    assert "Income_to_CreditRatio" in df.columns

def test_modelo_roda_sem_erros():
    # Treina modelo
    modelo_treinado = modelo.treinar_modelo("data/base_tratada.csv")

    # Verifica se objeto retornado é válido
    assert modelo_treinado is not None
