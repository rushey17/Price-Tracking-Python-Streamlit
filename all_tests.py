import yfinance as yf
import pandas as pd
from multipage_app.configs.constants import company_names_mappings

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
    print(company_dict)

def get_company_list():
    equity_details_df = pd.read_csv('nse_data/EQUITY_L.csv') 
    company_names = equity_details_df['NAME OF COMPANY'].tolist()
    print(company_names)

def get_symbol_by_company_name(company_name):
    return company_names_mappings.get(company_name)

def get_stock_data_by_date(company_name, start_date, end_date):
    symbol = get_symbol_by_company_name(company_name)
    equity_details_df = pd.read_csv(f'/multipage_app/nse_data/nse_stocks_data/{symbol}.csv') #Date,Open,High,Low,Close,Adj Close,Volume
    equity_details_df['Date'] = pd.to_datetime(equity_details_df['Date'])
    start_close_price = equity_details_df[equity_details_df['Date'] == start_date]['Close'].values[0]
    end_close_price = equity_details_df[equity_details_df['Date'] == end_date]['Close'].values[0]
    print(start_close_price)
    print(end_close_price)
    percentage_change = ((end_close_price - start_close_price) / start_close_price) * 100
    percentage_change_rounded = round(percentage_change, 2)
    print(percentage_change_rounded)



company_name = 'Reliance Industries Limited'
start_date = '2023-04-03'
end_date = '2023-04-13'
get_stock_data_by_date(company_name, start_date, end_date)