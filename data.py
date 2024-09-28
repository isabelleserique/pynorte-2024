import requests
import pandas as pd

def fetch_data(url="https://disease.sh/v3/covid-19/countries"):
    """
    Função para buscar dados da API da COVID-19.
    
    Parâmetros:
    url (str): URL da API de onde os dados serão buscados. 
               O padrão é o endpoint que retorna dados de todos os países.
    
    Retorna:
    list/dict: Os dados da API em formato JSON, se a requisição for bem-sucedida.
    None: Caso ocorra um erro durante a requisição.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve erro na resposta
        return response.json()  # Retorna os dados em formato JSON
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return None

def dataframe(data):
    """
    Converte os dados JSON em um DataFrame do pandas.
    
    Parâmetros:
    data (list/dict): Dados em formato JSON retornados pela API.
    
    Retorna:
    DataFrame: Um DataFrame do pandas com os dados normalizados.
               Se os dados forem nulos, retorna um DataFrame vazio.
    """
    if data:
        df = pd.json_normalize(data)
        return df
    else:
        return pd.DataFrame()

def table(df):
    """
    Filtra o DataFrame para exibir apenas dados da América do Sul.
    
    Parâmetros:
    df (DataFrame): DataFrame com os dados a serem manipulados.
    
    Retorna:
    DataFrame: Uma cópia do DataFrame filtrado com os países da América do Sul.
               Se o DataFrame estiver vazio, retorna o próprio DataFrame vazio.
    """
    if df.empty:
        print("DataFrame está vazio")
        return df
        
    #aqui voce pode aplicar quaisquer filtros na tabela que queira selecionar
    df_south_america = df[df['continent'] == 'South America'].copy()
    print(df_south_america)
    return df_south_america

def save_to_csv(df, file_name='table.csv'):
    """
    Salva o DataFrame em um arquivo CSV.
    
    Parâmetros:
    df (DataFrame): DataFrame que será salvo.
    file_name (str): Nome do arquivo CSV que será gerado (padrão é 'table.csv').
    
    Retorna:
    None: Apenas salva os dados no arquivo especificado ou emite uma mensagem
          se o DataFrame estiver vazio.
    """
    if not df.empty:
        df.to_csv(file_name, index=False)
        print(f"Dados salvos com sucesso em '{file_name}'")
    else:
        print("DataFrame vazio. Nenhum dado foi salvo.")

def main():
    """
    Função principal que coordena a execução do fluxo de trabalho:
    - Busca os dados da API
    - Converte os dados em DataFrame
    - Filtra para países da América do Sul
    - Salva os dados filtrados em um arquivo CSV
    """
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
