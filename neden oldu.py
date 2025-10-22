import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests 

url=pd.read_excel("C:\\Users\\buğra\\Desktop\\ne-olur\\hisseler_google_finance.xlsx")


print(url.columns)
""" aapl  """
tarih=url['Date']

hkodu={'Close', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOG', 'TSLA', 'PEP',
       'COST', 'AVGO', 'ADBE', 'NFLX', 'JPM', 'V', 'JNJ', 'UNH', 'XOM', 'NEE',
       'WMT', 'NKE', 'CAT', 'LMT', 'ASML', 'TSM', 'GS', 'PFE', 'SBUX', 'AMD'}
for hk in hkodu:
   ilk=url[hk].iloc[0]
   son=url[hk].iloc[-4]
   
   yüzdesel=((son -ilk)/ilk)*100
 
   print(f"{hk}: {yüzdesel}")

   
   sns.lineplot( x=tarih ,y=hk , data=url)
   plt.title(f"{hk} hisse senedi 2020-2025")
   plt.show()

NVDA: 2897.17
AVGO: 989.73
TSLA: 1431.76
TSM: 407.51
AMD: 374.70

