import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests 

url=pd.read_excel("C:\\Users\\buğra\\Desktop\\hisseler_google_finance (1).xlsx")


print(url.columns)
""" aapl  """
aapl=url['AAPL']
tarih=url['Date']

hkodu={'AAPL', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOG', 'TSLA', 'PEP',
       'COST', 'AVGO', 'ADBE', 'NFLX'}
for hk in hkodu:
   ilk=url[hk].iloc[0]
   son=url[hk].iloc[-4]
   
   yüzdesel=((son - ilk)/ilk )*100
   print(f"{hk}: {yüzdesel}")

   
   sns.lineplot( x=tarih ,y=hk , data=url)
   plt.title(f"{hk} hisse senedi 2020-2025")
   plt.show()



