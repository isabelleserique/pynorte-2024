import gspread
from google.oauth2 import service_account
import pandas as pd
import numpy as np

def get_google_sheets_credentials(path):
    """
    Autentica e retorna um cliente autorizado do Google Sheets.
    
    Parâmetros:
    path (str): Caminho para o arquivo de credenciais de serviço (JSON) necessário
                para acessar o Google Sheets via API.

    Retorna:
    gspread.Client: Um cliente autorizado do Google Sheets.
    """
    scope = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = service_account.Credentials.from_service_account_file(path, scopes=scope)
    return gspread.authorize(creds)
 
def get_or_create_spreadsheet(client, spreadsheet_id):
    """
    Abre uma planilha existente no Google Sheets ou cria uma nova se não for encontrada.

    Parâmetros:
    client (gspread.Client): Cliente autorizado do Google Sheets.
    spreadsheet_id (str): ID da planilha do Google Sheets.

    Retorna:
    gspread.Spreadsheet: Um objeto da planilha existente ou uma nova planilha criada.
    """
    try:
        return client.open_by_key(spreadsheet_id)
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Planilha com ID {spreadsheet_id} não encontrada. Criando uma nova.")
        return client.create(spreadsheet_id)

def transfer_data_to_worksheet(worksheet, df):
    """
    Transfere os dados de um DataFrame para uma worksheet do Google Sheets.
    
    Parâmetros:
    worksheet (gspread.Worksheet): A worksheet onde os dados serão inseridos.
    df (DataFrame): DataFrame com os dados a serem transferidos.

    Retorna:
    None: Apenas transfere os dados para a worksheet, formatando valores numéricos com 1 casa decimal.
    """
    df = df.applymap(lambda x: "{:.1f}".format(x) if np.issubdtype(type(x), np.number) else x)
    values = df.values.tolist()
    header = df.columns.values.tolist()
    worksheet.clear()  # Limpa a worksheet antes de inserir os novos dados
    worksheet.insert_row(header, 1)  # Insere o cabeçalho na primeira linha
    worksheet.insert_rows(values, 2)  # Insere os valores a partir da segunda linha

def read_csv(file_name):
    """
    Lê um arquivo CSV e o converte em um DataFrame.

    Parâmetros:
    file_name (str): Caminho para o arquivo CSV.

    Retorna:
    DataFrame: DataFrame contendo os dados lidos do arquivo CSV.
    """
    return pd.read_csv(file_name)

def main(publickey, spreadsheet_id, csv_file='table.csv'):
    """
    Função principal que gerencia a autenticação, leitura de dados e transferência para o Google Sheets.
    
    Parâmetros:
    publickey (str): Caminho para o arquivo de credenciais do Google API.
    spreadsheet_id (str): ID da planilha do Google Sheets onde os dados serão armazenados.
    csv_file (str): Caminho para o arquivo CSV contendo os dados a serem transferidos (padrão: 'table.csv').

    Retorna:
    None: Transfere os dados do CSV para o Google Sheets.
    """
    # Autentica o cliente do Google Sheets
    client = get_google_sheets_credentials(publickey)
    
    # Abre ou cria a planilha
    spreadsheet = get_or_create_spreadsheet(client, spreadsheet_id)
    
    # Lê o arquivo CSV e cria um DataFrame
    df = read_csv(csv_file)
    
    # Obtém a primeira worksheet da planilha
    worksheet = spreadsheet.get_worksheet(0)
    
    # Transfere os dados do DataFrame para a worksheet
    transfer_data_to_worksheet(worksheet, df)
    
    print(f"Dados do arquivo {csv_file} transferidos com sucesso para o Google Sheets.")

if __name__ == '__main__':
    publickey = '/home/iserique/Pynorte/credentials.json'  # Caminho para o arquivo de credenciais
    spreadsheet_id = '1U6cNm54fAz9BdADxXf2W71UZ1ujW0WhqTYruhouDRjA'  # ID da planilha no Google Sheets
    main(publickey, spreadsheet_id)
