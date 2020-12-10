import pandas as pd
import datetime as datetime

df = pd.read_excel('C:/Users/Jacob Steenhuysen/Downloads/chip tickers.xlsx', sheet_name='Sheet1')
#So just set up en excel file (not csv) and link the directory to above ^^^^^


#You're going to need to title the top of the column as Ticker or else this whole thing wont work.
tickers_list = df['Ticker'].tolist()
data = pd.DataFrame(columns=tickers_list)

import yfinance as yf
#for ticker in tickers_list:
#    data[ticker] = yf.download(ticker, period="5d", interval="1d") ["Close"]




for ticker in tickers_list:
    data[ticker] = yf.download(ticker, start=datetime.date(2015, 12, 30), end=datetime.date(2020, 12, 3), actions=True) ['Adj Close']
    #data[ticker] = yf.download(ticker, period = "5Y", interval = "1d")["Adj Close"]


export_excel = data.to_excel(r'C:/Users/Jacob Steenhuysen/Downloads/chipdata.xlsx', sheet_name='Sheet1', index= True)



