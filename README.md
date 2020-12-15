# AlgoTradingPython

### Algorithms for trading stocks from the S&P500
Requires at least an individual account at iexcloud.io. 
Run robust_value.py and hq-qantitative-momentum.py first. Then run value-weighted-by-momentum.py.

#### Robust Value
Calculates an aggregate value score and sorts on percentile. Metrics used are     'Price-to-Earnings Ratio',
    'Price-to-Book Ratio',
    'Price-to-Sales Ratio',
    'Enterprise-Value/EBITDA',
    and 'Enterprise-Value/Gross-Profit'.

#### HQ Quantitative Momentum
Calculates a high quality momentum score and sorts on percentile based on returns from 1 year, 6 months, 3 months, and one month.

#### Value Weighted By Momentum
Calculates a weighted score from HQ Quantitative Momentum averaged with Robust Value and sorts on percentile.
