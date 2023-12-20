
class ForexDataService():

    def __init__(self):
            pass

    def sayHi(self):
            return 'Hi from OANDA service module'

    def oanda_historical_data(instrument,start_date,end_date,granularity='D',client=None):
        params = {
            "from": start_date,
            "to": end_date,
            "granularity": granularity,
            "count": 2500,
        }

        df_full=pd.DataFrame()
        for r in InstrumentsCandlesFactory(instrument=instrument,params=params):
            client.request(r)
            dat = []
            api_data=r.response.get('candles')
            if(api_data):
                for oo in r.response.get('candles'):
                    dat.append([oo['time'], oo['volume'], oo['mid']['o'], oo['mid']['h'], oo['mid']['l'], oo['mid']['c']])

                df = pd.DataFrame(dat)
                df.columns = ['time', 'volume', 'open', 'high', 'low', 'close']
                df = df.set_index('time')
                if df_full.empty:
                    df_full=df
                else:
                    df_full=df_full.append(df)
        df_full.index=pd.to_datetime(df_full.index)    
        return df_full