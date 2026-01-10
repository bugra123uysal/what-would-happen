
import yfinance as yf
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime



ecl=[]

sy=["NVDA", "AAPL", "MSFT" , "AMZN", "GOOGL", "GOOG", "AVGO", "META", "TSLA","SPY","QQQ","DIA","IWM","VTI","IWM","IJH","XLK","XLF","XLV","XLE","XLY"]


""" bu günün tarih """
today=datetime.today().strftime('%Y-%m-%d')
for hisse in sy:


 al=yf.download(hisse, start="2020-01-01", end=today)
 tod_day=al["Close"].iloc[0] # başlangıç
 year_20=al["Close"].iloc[-1] #   2020 fiyatı


 getırı_1=(al["Close"].iloc[-1].item() / al["Close"].iloc[-252].item() -1) * 100 #  1 yıl
 getırı_2=(al["Close"].iloc[-1].item() / al["Close"].iloc[-252*2].item() - 1 ) * 100 #2 yıl
 getırı_3=(al["Close"].iloc[-1].item() / al["Close"].iloc[-252*3].item() - 1 ) * 100 #3 yıl
 getırı_4=(al["Close"].iloc[-1].item() / al["Close"].iloc[-252*4].item() - 1 ) * 100 #4 yıl
 getırı_5=(al["Close"].iloc[-1].item() / al["Close"].iloc[-252*5].item() - 1) * 100 #  5 yıl




 plt.plot(al["Close"])
 plt.title(f"{hisse} fiyat grafiği ")
 plt.show()





 ''' bilgiler '''
 bıl=yf.Ticker(hisse)
 hıs=bıl.info

 ecl.append({
    "Tarih":datetime.today().strftime('%y-%m-%d'),
    "Adı": hisse,
    "fiyat":hıs.get("currentPrice", None),
    "kapanış":al["Close"].iloc[-1].item(),
    "açılış":al["Open"].iloc[-1].item(),
    "5-yıllık":al["Close"],
    "volume": int(al["Volume"].iloc[-1]),
    "pe_oranı":hıs.get("trailingPE", None),
    "forward_pe":hıs.get("forwardPE", None),
    "peg_oranı":hıs.get("pegRatio", None),
    "kar_marjı":hıs.get("profitMargins", None),
    "eps":hıs.get("trailingEps", None),
    "sektör":hıs.get("sector",None),
    "endüstürü":hıs.get("industry",None),
    "piyasa_değeri":hıs.get("marketCap",None),
    "Website":hıs.get("website",None),
    "revenue_growth": hıs.get("revenueGrowth"),
    "earnings_growth": hıs.get("earningsGrowth"),
    "roe": hıs.get("returnOnEquity"),
    "roa": hıs.get("returnOnAssets"),
    "debt_to_equity": hıs.get("debtToEquity"),
    "current_ratio": hıs.get("currentRatio"),
    "free_cashflow": hıs.get("freeCashflow"),
    "operating_margin": hıs.get("operatingMargins"),
    "52w_high": hıs.get("fiftyTwoWeekHigh"),
    "52w_low": hıs.get("fiftyTwoWeekLow"),
    "avg_volume": hıs.get("averageVolume"),
    "beta": hıs.get("beta"),


    "1-yıl": int(round(getırı_1)),
    "2-yıl": int(round(getırı_2)),
    "3-yıl": int(round(getırı_3)),
    "4-yıl": int(round(getırı_4)),
    "5-yıl": int(round(getırı_5)),


})
gor=pd.DataFrame(ecl)
gor.to_excel("/content/drive/MyDrive/ecl.xlsx")


