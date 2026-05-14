import pandas as pd



print("Carregando base...")



df = pd.read_csv("data/base_original.csv")



# remover colunas que não vamos usar

colunas_remover = [

    "CLIENTNUM",

    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1",

    "Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2"

]



df.drop(columns=colunas_remover, inplace=True)



# salvar base limpa

df.to_csv("data/base_tratada.csv", index=False)



print("O arquivo 'base_tratada.csv' foi gerado dentro da pasta 'data'.")
