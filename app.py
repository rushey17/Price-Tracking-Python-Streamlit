# app.py

import streamlit as st
# from data import get_stock_data, plot_stock_data
from datetime import datetime, timedelta

st.set_page_config(page_title="Stock Price Tracker")
st.header("User Input")

with open("styles.css", "r") as f:
    custom_css = f.read()
st.markdown(f"<style>{custom_css}</style>", unsafe_allow_html=True)

# Input fields for stock symbol, start date, and end date
symbol = st.text_input("Enter stock symbol (e.g., AAPL)", value='AAPL', max_chars=5)
start_date = st.date_input("Start date", value=(datetime.now() - timedelta(days=365)).date())
end_date = st.date_input("End date", value=datetime.now().date())


if st.button("Fetch Data", key='fetch-button', help='Click to fetch stock data'):
    print(symbol)
    print(start_date)
    print(end_date)

# Fetch stock data
# stock_data = get_stock_data(symbol, start_date, end_date)

# # Display stock data
# if stock_data is None:
#     st.warning("No data found for the selected date range.")
# else:
#     st.title(f"Stock Price Tracker - {symbol}")
#     plot_stock_data(stock_data)
