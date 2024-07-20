# Backtest_struct

Defines functions Backtest, which accepts strategies. It provides the relevant data to the strategies, with strategies outputting a weighting dataframe; correpsonding to each stock and day.
The function will then calculate the returns using the portfolio weights from the strategy. The default stock universe is the S&P 500, but can be specified through the input of tickers.
