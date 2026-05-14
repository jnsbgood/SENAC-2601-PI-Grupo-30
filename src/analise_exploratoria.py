import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/base_tratada.csv")

print("Resumo estatístico")
print(df.describe())

# idade
plt.figure(figsize=(8,5))
sns.histplot(df["Customer_Age"], bins=20)

plt.title("Distribuição de Idade")
plt.show()

# churn
plt.figure(figsize=(6,4))
sns.countplot(
    x="Status_Cliente",
    data=df
)

plt.title("Clientes Ativos vs Cancelados")
plt.show()

# gênero
plt.figure(figsize=(6,4))
sns.countplot(
    x="Gender",
    hue="Status_Cliente",
    data=df
)

plt.title("Cancelamento por Gênero")
plt.show()
