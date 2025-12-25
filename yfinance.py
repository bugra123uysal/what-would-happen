
import yfinance as yf
import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime



ecl=[]

sy=["NVDA", "AAPL", "MSFT" , "AMZN", "GOOGL", "GOOG", "AVGO", "META", "TSLA",
     "LLY", "JPM", "WMT", "ORCL", "V", "XOM", "JNJ", "MA", "ABBV",
    "PLTR", "COST", "BAC", "AMD", "PG", "HD", "GE", "CVX", "UNH", "NFLX",
    "DIS", "KO", "PFE", "UNP", "TSM","MCD", "NKE", "SBUX", "CAT",
    "MMM", "MRK", "ABT", "LMT", "RTX", "GLW", "HON", "UPS"]


""" bu günün tarih """
today=datetime.today().strftime('%Y-%m-%d')
for hisse in sy:


 al=yf.download(hisse, start="2020-01-01", end=today)
 tod_day=al["Close"].iloc[0] # başlangıç
 year_20=al["Close"].iloc[-1] #   2020 fiyatı

 getırı_20=(al["Close"].iloc[-1] / al["Close"].iloc[0]- 1)*100 # 2020 den bu güne getiri
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
    "kapanış":al["Close"].iloc[-1],
    "açılış":al["Open"].iloc[-1],
    "5-yıllık":al["Close"].values,
    "hacim":al["Volume"].iloc[-1].values,
    "pe_oranı":hıs.get("trailingPE", None),
    "forward_pe":hıs.get("forwardPE", None),
    "peg_oranı":hıs.get("pegRatio", None),
    "kar_marjı":hıs.get("profitMargins", None),
    "eps":hıs.get("trailingEps", None),
    "sektör":hıs.get("sector",None),
    "endüstürü":hıs.get("industry",None),
    "piyasa_değeri":hıs.get("marketCap",None),
    "Website":hıs.get("website",None),
    "2020_getiri": getırı_20
})
gor=pd.DataFrame(ecl)
gor.to_excel("********")






