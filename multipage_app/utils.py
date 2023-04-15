import pandas as pd
import yfinance as yf
import streamlit as st

def get_ahead_date(date, days=1):
   timestamp_date_obj = pd.Timestamp(date)
   ahead_date_obj = timestamp_date_obj + pd.Timedelta(days=days)
   return str(ahead_date_obj).split(' ')[0]


# Define function to calculate percentage difference
def calculate_percentage_difference(stock_symbol, start_date, end_date):
    try:
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
        # Calculate percentage difference
        price_start = stock_data.iloc[0]['Close']
        price_end = stock_data.iloc[-1]['Close']
        percentage_diff = ((price_end - price_start) / price_start) * 100

        return price_start, price_end, percentage_diff
    except Exception as e:
        st.error(f"Error calculating percentage difference for {stock_symbol}: {e}")


# Define function to calculate result table with percentage difference
def calculate_result_table(selected_symbols, start_date, end_date):
    result_table = pd.DataFrame(columns=['Stock', 'Start Price', 'Current Price', 'Percentage Difference'])
    for stock_symbol in selected_symbols:
        price_start, price_end, percentage_diff = calculate_percentage_difference(stock_symbol, start_date, end_date)
        result_table = result_table.append({'Stock': stock_symbol,
                                            'Start Price': price_start,
                                            'Current Price': price_end,
                                            'Percentage Difference': percentage_diff}, ignore_index=True)
    return result_table