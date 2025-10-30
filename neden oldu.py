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

hkodu=['Close', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOG', 'TSLA'] 
for hk in hkodu:
   """ 5 yıllık """
   fi_5 = url[(url['Date'] >= '2020-01-03') & (url['Date'] <= '2025-10-24')]
   ilk=fi_5[hk].iloc[0]
   son=fi_5[hk].iloc[-1]
   
   fi_5_yüz=((son -ilk)/ilk)*100

 
   print(f"{hk}: {fi_5_yüz:.2f}%")

   
   """ 1 yıllık """
   fi_1=url[(url['Date'] >='2024-10-24') &(url['Date'] <='2025-10-23')]
   ilkk=fi_1[hk].iloc[0]
   sonn=fi_1[hk].iloc[-1]

   fi_1_yüz=((sonn - ilkk)/ilkk)*100

   print(f"1 yıllık {hk} değişim : {fi_1_yüz:.2f}%")

   """ 2 yıllık  """
   fi_2=url[(url['Date'] >="2023-10-24") & (url['Date'] <="2025-10-23")]

   ilk_2=fi_2[hk].iloc[0]
   son_2=fi_2[hk].iloc[-1]

   yüzde_2=((son_2 - ilk_2)/ilk_2)*100

   print(f"2 yıllık : {yüzde_2:.2f}%")

   "3 yıllık"

   fi_3=url[(url['Date'] >="2022-10-24") & (url['Date'] <="2025-10-23")]

   ilk_3=fi_3[hk].iloc[0]
   son_3=fi_3[hk].iloc[-1]

   yüz_3=((son_3 - ilk_3)/ilk_3)*100

   print(f"3 yıl : {yüz_3:.2f}%")

   "4 yıllık"
   fi_4=url[(url["Date"] >="2021-10-23") & (url['Date']  <="2025-10-23")]

   ilk_4=fi_4[hk].iloc[0]
   son_4=fi_4[hk].iloc[-1]

   yüz_4=((son_4 - ilk_4)/ ilk_4)*100
   tpu=yüz_4 * 1000
   print(tpu)

   print(f"4 yıllık : {yüz_4:.2f}%")


   sns.lineplot(x='Date' ,y=hk , data=url)
   plt.title(f"{hk} hisse senedi 2020-2025")
   plt.show()

    
aa=url.corr()
gg=aa[(aa > 0.6) & (aa < 1)]

print(gg.stack())
