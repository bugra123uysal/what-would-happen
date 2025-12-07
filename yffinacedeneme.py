
import yfinance as yf
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from numpy import info
from google.colab import  drive
import streamlit as st
from datetime import datetime
drive.mount("/content/drive")




ecl=[]

sy=["NVDA", "AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "AVGO", "META", "TSLA",
     "LLY", "JPM", "WMT", "ORCL", "V", "XOM", "JNJ", "MA", "ABBV",
    "PLTR", "COST", "BAC", "AMD", "PG", "HD", "GE", "CVX", "UNH", "NFLX",
    "DIS", "KO", "PFE", "UNP", "TSM","MCD", "NKE", "SBUX", "CAT",
    "MMM", "MRK", "ABT", "LMT", "RTX", "GLW", "HON", "UPS" ]





for hisse in sy:
 al=yf.download(hisse, start="2020-01-01", end="2025-12-03")



 sns.lineplot(al["Close"])
 plt.title(f"{hisse} 2020-2025 fiyat grafiği ")
 plt.show()

 ''' bilgiler '''
 bıl=yf.Ticker(hisse)
 hıs=bıl.info

 ecl.append({
    "Adı":hıs.get("longName", None),
    "fiyat":hıs.get("currentPrice", None),
    "kapanış":al["Close"].iloc[-1],
    "açılış":al["Open"].iloc[-1],
    "hacim":al["Volume"].iloc[-1],
    "sektör":hıs.get("sector",None),
    "endüstürü":hıs.get("industry",None),
    "piyasa_değeri":hıs.get("marketCap",None),
    "Website":hıs.get("website",None)
})
gor=pd.DataFrame(ecl)
gor.to_excel("/content/drive/MyDrive/ecl.xlsx")


