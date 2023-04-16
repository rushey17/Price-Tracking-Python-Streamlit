import yfinance as yf
import pandas as pd


def get_nse_stocks_data():
    equity_details = pd.read_csv('nse_data/EQUITY_L.csv') # All Details for NSE stocks : Symbol is the required field
    for name in equity_details.SYMBOL:
        try:
            data = yf.download(f'{name}.NS')
            data.to_csv(f'./nse_data/nse_stocks_data/{name}.csv') # Data will be stored in data folder
            print(f'{name} ===> completed')
        except Exception as e:
            print(f'{name} ===> {e}')

def map_symbols_with_name():
    equity_details_df = pd.read_csv('nse_data/EQUITY_L.csv') 
    equity_details_df.set_index('NAME OF COMPANY', inplace=True)
    company_dict = equity_details_df['SYMBOL'].to_dict()
    print(len(company_dict))

def get_company_list():
    equity_details_df = pd.read_csv('nse_data/EQUITY_L.csv') 
    company_names = equity_details_df['NAME OF COMPANY'].tolist()
    print(company_names)

get_company_list()