# Import required libraries
import yfinance as yf

# Define stock symbol and date range
symbol = 'AAPL'
start_date = '2023-04-01'
end_date = '2023-04-14'

stock_symbols = ['AAPL', 'MSFT', 'GOOGL']  # Example list of stock symbols

# Retrieve stock data for multiple symbols
stocks_data = yf.download(stock_symbols, start=start_date, end=end_date)

print(stocks_data)
# Calculate the percentage change for each stock
for stock_symbol in stock_symbols:
    stock_data = stocks_data[stock_symbol]
    price_at_start = stock_data['Close'][0]
    price_at_end = stock_data['Close'][-1]
    percentage_change = ((price_at_end - price_at_start) / price_at_start) * 100
    print(f"Percentage change for {stock_symbol} from {start_date} to {end_date}: {percentage_change:.2f}%")
