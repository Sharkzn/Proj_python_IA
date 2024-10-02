import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Ler arquivo csv pelo pandas
def ler_csv(file_path):
    return pd.read_csv(file_path)

def treinar(df):
    # Selecionando as colunas de entrada
    x = df[['acidez', 'densidade', 'viscosidade', 'tonalidade']]
    y = df['tipo_de_vinho']

    # Dividindo os dados em conjuntos de treino e teste
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    # Usando RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(x_train, y_train)

    # Avaliar modelo e sua precisão
    y_pred = model.predict(x_test)
    precisao = accuracy_score(y_test, y_pred)
    print(f"Precisão: {precisao * 100:.2f}%")

    return model

# Prever o vinho
def prever_vinho(model, acidez, densidade, viscosidade, tonalidade):
   # Criar um Dataframe com o mesmo estrutura usada no trainamento
    entrada = pd.DataFrame({
        'acidez': [acidez],
        'densidade': [densidade],
        'viscosidade': [viscosidade],
        'tonalidade': [tonalidade]
        
    })
    predicao = model.predict(entrada)
    probabilidade = model.predict_proba(entrada)
    return predicao[0], max(probabilidade[0]) * 100

# Método Principal
if __name__ == "__main__":
    # Variável que armazena nome do arquivo csv
    arquivo = 'vinhos.csv'
    df = ler_csv(arquivo)
    model = treinar(df)

    # Entrada de dados pelo usuário
    acidez = 0.55
    densidade = 0.85
    viscosidade = 0.45
    tonalidade = 0.9

    # Prever tipo de vinho
    tipo, prob = prever_vinho(model, acidez, densidade, viscosidade, tonalidade)
    print(f'Tipo de vinho previsto: {tipo}, com probabilidade de {prob:.2f}%')
    
