# Ticker-History-Scraper
So this is a scraper I wish I had when I started finance. It's just a standard price scraper. It can get Adj Close, Close and Dividends. 
It takes a list of tickers from a pandas dataframe and then runs them through yfinance and grabs what is needed and appends the dataframe and writes
it into an excel file for you.

You need to pip install yfinance and pandas.
