import pandas as pd



from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score





def treinar_modelo(caminho_base="data/base_tratada.csv"):

    df = pd.read_csv(caminho_base)



    df["Churn"] = df["Attrition_Flag"].map({

        "Existing Customer": 0,

        "Attrited Customer": 1

    })



    X = df[

        [

            "Customer_Age",

            "Months_Inactive_12_mon",

            "Total_Trans_Ct",

            "Credit_Limit",

            "Income_to_CreditRatio"

        ]

    ]



    y = df["Churn"]



    X_train, X_test, y_train, y_test = train_test_split(

        X,

        y,

        test_size=0.3,

        random_state=42

    )



    modelo = LogisticRegression(max_iter=1000)



    modelo.fit(X_train, y_train)



    predicoes = modelo.predict(X_test)



    acuracia = accuracy_score(y_test, predicoes)



    print(f"Acurácia do modelo: {acuracia:.2f}")



    return modelo





if __name__ == "__main__":

    treinar_modelo("data/base_tratada.csv")
