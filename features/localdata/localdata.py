import pandas as pd
class LocalData:
    def __init__(self,timeframe,pair,account,platform):
       self.timeframe = timeframe
       self.pair = pair
       self.account = account
       self.platform = platform

    def loadData(self):
        path = self.getPath()
        df = pd.read_csv(path)
        return df

    def getPath(self):
        if(self.account == "real" or self.account == "REAL"):
            return r"C:\Users\User\AppData\Roaming\MetaQuotes\Terminal\86ADC2D106E3946A8F8D9E6D2FD89531\MQL5\Files\History (OctaFX-Real2)\{}{}.csv".format(self.pair,self.timeframe)
        
    def renameColumn(self):
        column = ["Date","Time","Open","High","Low","Close","Volume"]
        return column
    
    def mergeDataAndColumn(self):
        df = self.loadData()
        column = self.renameColumn()
        df.columns = column
        return df