import gspread
from google.oauth2 import service_account
import pandas as pd
import numpy as np

def get_google_sheets_credentials(path):
   scope = ["https://www.googleapis.com/auth/spreadsheets"]
   creds = service_account.Credentials.from_service_account_file(path, scopes=scope)
   return gspread.authorize(creds)
 
def get_or_create_spreadsheet(client, spreadsheet_id):
    try:
        return client.open_by_key(spreadsheet_id)
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Spreadsheet with ID {spreadsheet_id} not found. Creating a new one.")
        return client.create(spreadsheet_id)

def transfer_data_to_worksheet(worksheet, df):
    df = df.applymap(lambda x: "{:.1f}".format(x) if np.issubdtype(type(x), np.number) else x)
    values = df.values.tolist()
    header = df.columns.values.tolist()
    worksheet.clear()
    worksheet.insert_row(header, 1)
    worksheet.insert_rows(values, 2)

def read_csv(file_name):
    return pd.read_csv(file_name)

def main(publickey, spreadsheet_id, csv_file='table.csv'):
    client = get_google_sheets_credentials(publickey)
    spreadsheet = get_or_create_spreadsheet(client, spreadsheet_id)
    df = read_csv(csv_file)
    worksheet = spreadsheet.get_worksheet(0)
    transfer_data_to_worksheet(worksheet, df)
    print(f"Dados do arquivo {csv_file} transferidos com sucesso para o Google Sheets.")
    
if __name__ == '__main__':
    publickey = '/home/iserique/Pynorte/credentials.json'
    spreadsheet_id = '1U6cNm54fAz9BdADxXf2W71UZ1ujW0WhqTYruhouDRjA'
    main(publickey, spreadsheet_id)
