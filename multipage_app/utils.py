import pandas as pd
import yfinance as yf
import streamlit as st
from configs.constants import company_names_mappings


def get_ahead_date(date, days=1):
   timestamp_date_obj = pd.Timestamp(date)
   ahead_date_obj = timestamp_date_obj + pd.Timedelta(days=days)
   return str(ahead_date_obj).split(' ')[0]


# Define function to calculate percentage change
def calculate_percentage_change(company_name, start_close_price, end_close_price):
   try:
      percentage_change = ((end_close_price - start_close_price) / start_close_price) * 100
      return round(percentage_change, 2)
   except Exception as e:
      st.error(f"Error calculating percentage change for {company_name}: {e}")


# Define function to calculate result table with percentage difference
def calculate_result_table(selected_stocks, start_date, end_date):
   result_table_df = pd.DataFrame(columns=['Stock', 'Start Date Price', 'End Date Price', 'Percentage Change'])
   for stock_name in selected_stocks:
      start_close_price, end_close_price, percentage_change = get_stock_data_by_date(stock_name, start_date, end_date)
      result_table_df = result_table_df.append({'Stock': stock_name,
                                            'Start Date Price': start_close_price,
                                            'End Date Price': end_close_price,
                                            'Percentage Change': percentage_change}, ignore_index=True)
   return result_table_df


def get_symbol_by_company_name(stock_name):
   return company_names_mappings.get(stock_name)


def get_stock_data_by_date(stock_name, start_date, end_date):
   stock_symbol = get_symbol_by_company_name(stock_name)
   equity_details_df = pd.read_csv(f'./nse_data/nse_stocks_data/{stock_symbol}.csv') #Date,Open,High,Low,Close,Adj Close,Volume
   equity_details_df['Date'] = pd.to_datetime(equity_details_df['Date'])
   equity_details_df.set_index('Date', inplace=True)
   start_close_price = round(equity_details_df.loc[start_date, 'Close'], 2)
   end_close_price = round(equity_details_df.loc[end_date, 'Close'], 2)
   percentage_change = calculate_percentage_change(stock_name, start_close_price, end_close_price)
   print(start_close_price, end_close_price, percentage_change)
   return start_close_price, end_close_price, percentage_change    