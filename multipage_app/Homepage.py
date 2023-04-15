import streamlit as st
import pandas as pd
import yfinance as yf

st.set_page_config(
    page_title="FreeBreakouts.com"
)
st.title("Check Your Investment!")

# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

stock_symbols = ['AAPL', 'GOOGL', 'AMZN', 'TSLA', 'MSFT', 'NFLX', 'FB', 'NVDA', 'PYPL', 'AMGN', 'RELIANCE.NS', 'HDFC.NS']
# Get user inputs
selected_symbols = st.multiselect("Select stock symbols", options=stock_symbols, default=['AAPL'])
start_date = st.date_input("Select start date", value=pd.Timestamp('2022-01-01'))
end_date = st.date_input("Select end date", value=pd.Timestamp('2023-04-15'))

# Define function to calculate percentage difference
def calculate_percentage_difference(stock_symbol, start_date, end_date):
    try:
        # Download stock data using yfinance
        stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

        # Calculate percentage difference
        price_start = stock_data.iloc[0]['Close']
        price_end = stock_data.iloc[-1]['Close']
        percentage_diff = ((price_end - price_start) / price_start) * 100

        return price_start, price_end, percentage_diff
    except Exception as e:
        st.error(f"Error calculating percentage difference for {stock_symbol}: {e}")

# Calculate percentage difference for each selected stock
if st.button("Calculate"):
    with st.spinner("Loading data..."):
        # Loop through selected stock symbols
        result_table = pd.DataFrame(columns=['Stock', 'Start Price', 'Current Price', 'Percentage Difference'])
        for stock_symbol in selected_symbols:
            # Call the function to calculate percentage difference
            price_start, price_end, percentage_diff = calculate_percentage_difference(stock_symbol, start_date, end_date)

            # Add results to the result table
            result_table = result_table.append({'Stock': stock_symbol,
                                                'Start Price': price_start,
                                                'Current Price': price_end,
                                                'Percentage Difference': round(percentage_diff, 2)}, ignore_index=True)

        # Display results in a table
        st.table(result_table)
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

# st.table(df)