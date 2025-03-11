from os import times
from polygon import RESTClient
from datetime import datetime

import pandas as pd

client = RESTClient('0fDpHNdN_o2AV3Yg9d4KCJ5h2v82xdJk')

ticker     = 'C:EURUSD'
multiplier = 1
timespan   = 'hour'
from_      = datetime(2010, 1, 1)
to = datetime(2023, 12, 30)

data = client.get_aggs(
      ticker, 
      multiplier, 
      timespan, 
      from_, 
      to, 
      adjusted=None, 
      sort=None, 
      limit=None, 
      params=None, 
      raw=False, 
      options=None
)

df = pd.DataFrame(data)
df['Date']=df['timestamp'].apply(lambda x: pd.to_datetime(x*1000000))
df.set_index('Date', inplace=True)


print(df)