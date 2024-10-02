import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Ler arquivo csv pelo pandas
def ler_csv(file_path):
    return pd.read_csv(file_path)

def treinar(df):
    # Selecionando as colunas de entrada
    x = df[['Acidez','Densidade','Viscosidade','tonalidade']]
    y = df['tipo_de_vinho']

    # Dividindo os dados em dois tipos de treinos 
    x_train = train_test_split(x,y, test_size=0.2, random_state=42)
    x_test = train_test_split(x,y, test_size=0.2, random_state=42)
    y_train = train_test_split(x,y, test_size=0.2, random_state=42)
    y_test = train_test_split(x,y, test_size=0.2, random_state=42)

    # Usando Random como exemplo
    model= RandomForestClassifier()
    model.fit(x_train,y_train)

    #avaliar modelo e sua precisão
    y_pred = model.predict(x_test)
    precisão = accuracy_score(y_test,y_pred)
    print(f"Precisão: {precisão * 100:.2f}%")

    return model

# Prever o vinho
def prever_vinho(Model,Acidez,Densidade,Viscozidade,Tonalidade):
    entrada = [[Acidez,Densidade,Viscozidade,Tonalidade]]
    predicao = Model.predict(entrada)
    probalidade  = Model.predict_proba(entrada)

    return predicao[0],max(probalidade[0])*100
# Metodo Principal
if __name__ == "__main__":
    #Variavel que armazena nome do arquivo csv
    arquivo = 'vinhos.csv'
    df = ler_csv(arquivo)
    model = treinar(df)

    # Entrada de dados pelo usuario
    acidez = float(input('Valor de Acidez: '))
    Densidade = float(input('Valor de Densidade: '))
    Viscozidade = float(input('Valor de Viscozidade: '))
    Tonalidade = float(input('Valor de Tonalidade: '))
    
