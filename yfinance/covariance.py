import yfinance as yf
import pandas as pd

def fetch_stock_data(tickers, start_date, end_date):
    stock_data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return stock_data

def calculate_covariance(stock_data):
    covariance_matrix = stock_data.cov()
    return covariance_matrix

tickers = ['AAPL', 'MSFT', 'GOOGL']
start_date = '2023-01-01'
end_date = '2023-07-01'

stock_data = fetch_stock_data(tickers, start_date, end_date)
covariance_matrix = calculate_covariance(stock_data)

print(f"공분산 행렬 ({start_date} ~ {end_date}):")
print(covariance_matrix)
