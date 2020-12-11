import numpy as np
import pandas as pd
import requests
from scipy import stats
import xlsxwriter
from secrets import IEX_CLOUD_API_TOKEN
from dry import symbolStrings, sharesToBuy

stocks = pd.read_csv('sp_500_stocks.csv')
symbol = 'AAPL'
api_url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/stats/stats?token={IEX_CLOUD_API_TOKEN}'
data = requests.get(api_url).json()
symbol_strings = symbolStrings(stocks)
columns = ['Ticker', 'Stock Price', 'One-Year Price Return', 'Number of Shares to Buy']
df = pd.DataFrame(columns=columns)
for symbol_string in symbol_strings:
    batch_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch?symbols={symbol_string}&types=price,stats&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_call_url).json()
    for symbol in symbol_string.split(','):
        df = df.append(
            pd.Series(
                [
                    symbol,
                    data[symbol]['price'],
                    data[symbol]['stats']['year1ChangePercent'],
                    'N/A'
                ],
                index=columns
            ),
            ignore_index=True
        )
df.sort_values('One-Year Price Return', ascending=False, inplace=True)
df = df[:50]
df.reset_index(inplace=True)

df = sharesToBuy(df)
print(df)