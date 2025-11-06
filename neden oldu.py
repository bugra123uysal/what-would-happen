import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests 
import streamlit as st
url=pd.read_excel("C:\\Users\\buğra\\Desktop\\ne-olur\\hisseler_google_finance (6).xlsx", header=1)

one_hun=[]

""" 

hkodu=['Close', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOG', 'TSLA', 'PEP',
       'COST', 'AVGO', 'ADBE', 'NFLX', 'JPM', 'V', 'JNJ', 'UNH', 'XOM', 'NEE',
       'WMT', 'NKE', 'CAT', 'LMT', 'ASML', 'TSM', 'GS', 'PFE', 'SBUX', 'AMD'] 
 """
print(url.columns)
""" aapl  """
tarih=url["Date"]
url['TSLA']=url['TSLA'].fillna(method='ffill')
url['AMZN']=url['AMZN'].fillna(method='ffill')
print(url.isnull().sum())
url['Date']=pd.DataFrame(url['Date'])

hkodu=['Close', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOG', 'TSLA'] 
for hk in hkodu:
   """ 5 yıllık """
   fi_5 = url[(url['Date'] >= '2020-01-03') & (url['Date'] <= '2025-10-28')]
   ilk=fi_5[hk].iloc[0]
   son=fi_5[hk].iloc[-1]
   
   fi_5_yüz=((son -ilk)/ilk)*100

 
   print(f"{hk}: {fi_5_yüz:.2f}%")

   
   """ 1 yıllık """
   fi_1=url[(url["Date"] >='2024-10-28') &(url['Date'] <='2025-10-28')]
   ilkk=fi_1[hk].iloc[0]
   sonn=fi_1[hk].iloc[-1]

   fi_1_yüz=((sonn - ilkk)/ilkk)*100

   print(f"1 yıllık {hk} değişim : {fi_1_yüz:.2f}%")

   """ 2 yıllık  """
   fi_2=url[(url['Date'] >="2023-10-28") & (url['Date'] <="2025-10-28")]

   ilk_2=fi_2[hk].iloc[0]
   son_2=fi_2[hk].iloc[-1]

   fi_2_yüz=((son_2 - ilk_2)/ilk_2)*100

   print(f"2 yıllık : {fi_2_yüz:.2f}%")

   "3 yıllık"

   fi_3=url[(url['Date'] >="2022-10-28") & (url['Date'] <="2025-10-28")]

   ilk_3=fi_3[hk].iloc[0]
   son_3=fi_3[hk].iloc[-1]

   fi_3_yüz=((son_3 - ilk_3)/ilk_3)*100

   print(f"3 yıl : {fi_3_yüz:.2f}%")

   "4 yıllık"
   fi_4=url[(url["Date"] >="2021-10-28") & (url['Date']  <="2025-10-28")]

   ilk_4=fi_4[hk].iloc[0]
   son_4=fi_4[hk].iloc[-1]

   fi_4_yüz=((son_4 - ilk_4)/ ilk_4)*100



   print(f"4 yıllık : {fi_4_yüz:.2f}%")
   
   sns.lineplot(x='Date' ,y=hk , data=url)
   plt.title(f"{hk} hisse senedi 2020-2025")
   plt.show()
    
   """ paraya ne olur   1000$"""

   money=1000
   """ yg:yıllık getiri """
   yg=[fi_1_yüz ,fi_2_yüz,  fi_3_yüz, fi_4_yüz,  fi_5_yüz]

   for  yy in yg:

 
     money *=(1 + yy/100)
     print(f"{yy}. yıl:{money:.2f}")

     one_hun.append({
     "Hisse": hk,
     "1 yıllık(%)":round(fi_1_yüz,2),
     "2 yıllık(%)":round(fi_2_yüz,2),
     "3 yıllık(%)":round(fi_3_yüz,2),
     "4 yıllık(%)":round(fi_4_yüz,2),
     "5 yıllık(%)":round(fi_5_yüz,2),
     " 1000 dollara ne oldu(%)": round(money,2),
        
     })

snc=pd.DataFrame(one_hun)
snc.to_excel("C:\\Users\\buğra\\Desktop\\ne-olur\\1000_dollar.xlsx", index=False)




aa=url.corr()
gg=aa[(aa > 0.6) & (aa < 1)]

print(gg.stack())
