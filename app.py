import streamlit as st
import yfinance as yf
import pandas as pd
import datetime as dt

class StockTracker:
    def __init__(self, symbol, start_date):
        self.symbol = symbol
        self.start_date = start_date
        self.df = None

    def get_data(self):
        end_date = dt.date.today()
        try:
            self.df = yf.download(self.symbol, start=self.start_date, end=end_date)
        except Exception as e:
            st.write(f"Error: {e}")

    def get_performance(self, days):
        perf = (self.df.iloc[-1]['Close'] / self.df.iloc[-days]['Close'] - 1) * 100
        return round(perf, 2)

    def get_portfolio_value(self, investment):
        curr_price = self.df.iloc[-1]['Close']
        shares = investment / curr_price
        value = shares * curr_price
        return round(value, 2)

def create_tracker(symbol, start_date):
    tracker = StockTracker(symbol, start_date)
    tracker.get_data()
    return tracker

st.title("Stock Price Tracker")
symbol = st.text_input("Enter stock symbol (e.g. AAPL):")
start_date = st.date_input("Enter start date:")
investment = st.number_input("Enter investment amount:", min_value=0, value=10000, step=100)
tracker = create_tracker(symbol, start_date)

if tracker.df is None:
    st.write("Error: could not retrieve data for the specified symbol and start date")
else:
    st.write(f"Showing data for {symbol} from {start_date} to {dt.date.today()}")
    st.write(tracker.df)

    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            st.write(f"Performance last 7 days: {tracker.get_performance(7)}%")
        except Exception as e:
            st.write(f"Error: {e}")
    with col2:
        month_perf = st.slider("Select number of months:", min_value=1, max_value=12, value=1)
        try:
            st.write(f"Performance last {month_perf} month(s): {tracker.get_performance(30 * month_perf)}%")
        except Exception as e:
            st.write(f"Error: {e}")
    with col3:
        try:
            st.write(f"Portfolio value: {tracker.get_portfolio_value(investment)}")
        except Exception as e:
            st.write(f"Error: {e}")
