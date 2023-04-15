import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(
    page_title="FreeBreakouts.com"
)

import utils
from styles.st_styles import hide_table_row_index

st.title("Check Your Investment!")
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

stock_symbols = ['AAPL', 'GOOGL', 'AMZN', 'TSLA', 'MSFT', 'NFLX', 'FB', 'NVDA', 'PYPL', 'AMGN', 'RELIANCE.NS', 'HDFC.NS']
# Get user inputs
selected_symbols = st.multiselect("Select stock symbols", options=stock_symbols, default=['AAPL'])
start_date = st.date_input("Select start date")
end_date = st.date_input("Select end date")

# Calculate percentage difference for each selected stock
if st.button("Calculate"):
    with st.spinner("Loading data..."):
        result_table = utils.calculate_result_table(selected_symbols, start_date, end_date)
        st.table(result_table)

