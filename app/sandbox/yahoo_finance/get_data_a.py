import os
import numpy as np
import pandas as pd
import datetime as dt
from pandas_datareader import data as pdr

import yfinance as yfin
yfin.pdr_override()

def get_mkt_data(ticker, start, end, interval):
  
    df = pdr.get_data_yahoo(ticker, start=start, end=end, interval=interval)
    return df


data =get_mkt_data('JPY=X', '2010-01-01', '2023-12-30', '1d')
print(data)
