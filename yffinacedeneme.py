import finnhub 
import pandas as pd
import requests
from datetime import datetime 
api="cp7rd3pr01qi8q89arpgcp7rd3pr01qi8q89arq0"
sy=["NVDA", "AAPL", "MSFT", "AMZN", "GOOGL", "GOOG", "AVGO", "META", "TSLA",
    "BRK.B", "LLY", "JPM", "WMT", "ORCL", "V", "XOM", "JNJ", "MA", "ABBV",
    "PLTR", "COST", "BAC", "AMD", "PG", "HD", "GE", "CVX", "UNH", "NFLX",
    "DIS", "KO", "PFE", "UNP", "TSM","MCD", "NKE", "SBUX", "CAT",
    "MMM", "MRK", "ABT", "LMT", "RTX", "GLW", "HON", "UPS"]


ecl=[]

for  symbol in sy:
    url=f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api}"
    data=requests.get(url).json()
    timestamp=data.get("t",None)
    date=datetime.fromtimestamp(timestamp).strftime("%y-%m-%d") if timestamp else None
    
    ecl.append({
        "symbol": symbol,
        "Date": date,
        "Open": data.get("o", None),
        "Close": data.get("c",None),
        "High": data.get("h", None),  
        "Low": data.get("l", None),
        "Volume": data.get("v", None),
       
    })
   

gor=pd.DataFrame(ecl)
gor.to_excel("C:\\Users\\buğra\\Desktop\\portfoyy.xlsx")

