import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests 

url=pd.read_excel("C:\\Users\\buğra\\Desktop\\ne-olur\\hisseler_google_finance.xlsx")

""" 

hkodu=['Close', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOG', 'TSLA', 'PEP',
       'COST', 'AVGO', 'ADBE', 'NFLX', 'JPM', 'V', 'JNJ', 'UNH', 'XOM', 'NEE',
       'WMT', 'NKE', 'CAT', 'LMT', 'ASML', 'TSM', 'GS', 'PFE', 'SBUX', 'AMD'] 
 """
print(url.columns.str.strip())
""" aapl  """
tarih=url['Date']
url['TSLA']=url['TSLA'].fillna(method='ffill')
url['AMZN']=url['AMZN'].fillna(method='ffill')
print(url.isnull().sum())
url['Date']=pd.DataFrame(url['Date'])
filtre=url[(url['Date'] >='2024-10-24') &(url['Date'] <='2025-10-24')]

hkodu=['Close', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOG', 'TSLA'] 
for hk in hkodu:
   
   fi = url[(url['Date'] >= '2020-01-03') & (url['Date'] <= '2025-10-22')]


   ilk=fi[hk].iloc[0]
   son=fi[hk].iloc[-1]
   
   yüzdesel=((son -ilk)/ilk)*100

   mac_50=url[hk].rolling(window=50).mean()
   mac_200=url[hk].rolling(window=200).mean()
   print(f"{hk}: 50 günlük: {mac_50}")
   print(f"{hk}: 200 günlük: {mac_50}")
   print(f"{hk}: {yüzdesel:.2f}%")
   """ 1 yıllık """

   ilkk=filtre[hk].iloc[0]
   sonn=filtre[hk].iloc[-1]

   yuz=((sonn - ilkk)/ilkk)*100
     
   print(f"1 yıllık {hk} değişim : {yuz:.2f}%")
   
   


   sns.lineplot(x='Date' ,y=hk , data=url)
   plt.title(f"{hk} hisse senedi 2020-2025")
   plt.show()
    
aa=url.corr()
print(aa)
