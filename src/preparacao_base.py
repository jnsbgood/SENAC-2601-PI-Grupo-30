import pandas as pd

df = pd.read_csv('./data/base_original.csv')

colunas_para_remover = [
    'CLIENTNUM',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1',
    'Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2'
]

df_tratado = df.drop(columns=colunas_para_remover)

df_tratado.to_csv('./data/base_tratada.csv', index=False)

print("O arquivo 'base_tratada.csv' foi gerado dentro da pasta 'data'.")