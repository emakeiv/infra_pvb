import backtrader as bt
import datetime



if __name__ == "__main__":

      cerebro = bt.Cerebro()
      data = bt.feeds.GenericCSVData(
            dataname="../data/AAPL.csv",
            separator = ',',
            dtformat ="%Y-%m-%d",
            fromdate=datetime.datetime(2018, 1, 2),
            todate=datetime.datetime(2021, 12, 31)

      )
      cerebro.adddata(data)
      cerebro.broker.setcash(1000000)

      print(f"Starting porfolio value: {cerebro.broker.getvalue():.2f}")
      cerebro.run()
      print(f"Final porfolio value: {cerebro.broker.getvalue():.2f}")
      