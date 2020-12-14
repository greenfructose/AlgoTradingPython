import numpy as np
import pandas as pd
import requests
from scipy import stats
from statistics import mean
import xlsxwriter
from secrets import IEX_CLOUD_API_TOKEN
from dry import symbolStrings, sharesToBuy

stocks = pd.read_csv('sp_500_stocks.csv')
symbol_strings = symbolStrings(stocks)
columns = [
    'Ticker',
    'Stock Price',
    'Price-to-Earnings Ratio',
    'Number of Shares to Buy'
]
df = pd.DataFrame(columns=columns)
for symbol_string in symbol_strings:
    batch_call_url = f'https://sandbox.iexapis.com/stable/stock/market/batch/?types=quote&symbols={symbol_string}&token={IEX_CLOUD_API_TOKEN}'
    data = requests.get(batch_call_url).json()
    for symbol in symbol_string.split(','):
        df = df.append(
            pd.Series(
                [
                    symbol,
                    data[symbol]['quote']['latestPrice'],
                    data[symbol]['quote']['peRatio'],
                    'N/A'
                ],
                index=columns
            ),
            ignore_index=True
        )
df.sort_values('Price-to-Earnings Ratio', inplace=True)
df = df[df['Price-to-Earnings Ratio'] > 0]
df.reset_index(inplace=True, drop=True)
df = df[:50]
df = sharesToBuy(df)
print(df)