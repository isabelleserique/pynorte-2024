import requests
import pandas as pd

def fetch_data(url="https://disease.sh/v3/covid-19/countries"):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na resposta
        return response.json()  # Retorna os dados em formato JSON
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

def dataframe(data):
    if data:
        df = pd.json_normalize(data)
        return df
    else:
        return pd.DataFrame()

def table(df):
    if df.empty:
        print("DataFrame está vazio")
        return df
    
    df_south_america = df[df['continent'] == 'South America'].copy()
    table = df_south_america.copy()
    print(table)
    return table

def save_to_csv(df, file_name='table.csv'):
    if not df.empty:
        df.to_csv(file_name, index=False)
        print(f"Dados salvos com sucesso em '{file_name}'")
    else:
        print("DataFrame vazio. Nenhum dado foi salvo.")

def main():
    # Busca os dados da API
    data = fetch_data()

    # Cria o DataFrame
    df = dataframe(data)

    # Manipula a tabela (filtrando América do Sul)
    manipulated_df = table(df)

    # Salva a tabela manipulada em CSV
    save_to_csv(manipulated_df)

if __name__ == "__main__":
    main()
