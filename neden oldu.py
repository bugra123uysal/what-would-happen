import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime
 # hisse fiyatları 
url=pd.read_excel(f"C:\\Users\\buğra\\Desktop\\ne-olur\hisseler_google_finance.xlsx")
#hisse bilgileri 
al=pd.read_excel(f"C:\\Users\\buğra\\Desktop\\ne-olur\\hisseler_hakkında_başka_bilgiler.xlsx")
print(al.columns)

one_hun=[]


hkodu=['Close', 'MSFT', 'AMZN', 'NVDA', 'META', 'GOOG', 'TSLA', 'PEP','COST', 'AVGO', 'ADBE', 'NFLX', 'JPM', 'V', 'JNJ', 'UNH', 'XOM', 'NEE','WMT', 'NKE', 'CAT', 'LMT', 'ASML', 'TSM', 'GS', 'PFE', 'SBUX', 'AMD'] 
 
print(url.columns)
url["Date"]=pd.to_datetime(url['Date'])


print(url.isnull().sum())

""" bileşik faiz """
 
hıs_bılgı=['Volume', 'Marketcap', 'Pe', 'Eps', 'Günlük_Değişim',
       'Hisse_adet', 'Beta', '52 haftalık en yüksek fiyat',
       '52 haftalık en düşük fiyat']

"""  açılı menü """

""" bütce """
main_money = [1000, 2000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 100000, 150000]
m_money=st.selectbox("ana para seçiniz", main_money)

""" yıllık getiri  """
yıllık_getiri=[0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.90, 1.00]
y_getiri=st.selectbox("Getiri seçini:",yıllık_getiri)

""" yıl """

yıl = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

yyyıl=st.selectbox("süre seçiniz", yıl)

"""  bileşik faiz hesapmlam  """

bileşik=m_money *(1 + y_getiri) ** yyyıl




if st.button("send ballons"):
  st.write(bileşik)
  st.balloons()

hk=st.selectbox(":", hkodu)
url[hk]=url[hk].fillna(method='ffill')
#1 yıllık 
""" bu günün tarih """
today=datetime.today().strftime('%Y-%m-%d')

fi_1=url[(url["Date"] >='2024-10-28') &(url['Date'] <= today )]
ilkk=fi_1[hk].iloc[0]
sonn=fi_1[hk].iloc[-1]
fi_1_yüz=((sonn / ilkk) ** (1/1) - 1 )* 100
st.write(f"{hk} 1 yılda : {fi_1_yüz:.2f}%")

   
   # 2 yıllık 
fi_2=url[(url['Date'] >="2023-10-28") & (url['Date'] <= today)]
ilk_2=fi_2[hk].iloc[0]
son_2=fi_2[hk].iloc[-1]
fi_2_yüz=((son_2 / ilk_2) ** (1/2) - 1)* 100
st.write(f"{hk} 2 yılda : {fi_2_yüz:.2f}%")

# 3 yıllık
fi_3=url[(url['Date'] >="2022-10-28") & (url['Date'] <=today )]
ilk_3=fi_3[hk].iloc[0]
son_3=fi_3[hk].iloc[-1]
fi_3_yüz=((son_3 / ilk_3) ** (1/3) -1 )*100
st.write(f"{hk} 3 yılda :{fi_3_yüz:.2f}%")

# 4 yıllık
fi_4=url[(url["Date"] >="2021-10-28") & (url['Date']  <= today)]
ilk_4=fi_4[hk].iloc[0]
son_4=fi_4[hk].iloc[-1]
fi_4_yüz=((son_4 / ilk_4) ** (1/4) - 1 )*100
st.write(f"{hk} 4 yılda : {fi_4_yüz:.2f}%")

# 5 yıllık 
fi_5 = url[(url['Date'] >= '2020-01-03') & (url['Date'] <= today)]
ilk=fi_5[hk].iloc[0] 
son=fi_5[hk].iloc[-1]

fi_5_yüz=((son / ilk) ** (1/5) - 1 )*100
st.write(f"{hk} 5 yılda : {fi_5_yüz:.2f}%")

fig, ax =plt.subplots()

sns.lineplot(x='Date' ,y=hk , data=url)
ax.set_title(f"{hk}  hissesinin 2020-2025 grafiği")
ax.set_xlabel=("Hisse")
ax.set_ylabel=("aa")
plt.grid(True)
st.pyplot(fig)


for  kh in hıs_bılgı:
    
   st.write(f"Hisse {hk}")
   fig , ax=plt.subplots()
   sns.countplot(kh)
   ax.set_xlabel("Hisse")
   ax.set_ylabel(hıs_bılgı)
   st.pyplot(fig)


"""  birleşik getiri hesaplma """



aa=url.corr()
gg=aa[(aa > 0.6) & (aa < 1)]

print(gg.stack())

