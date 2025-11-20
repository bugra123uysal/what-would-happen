import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
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


hıs_bılgı=['Volume', 'Marketcap', 'Pe', 'Eps', 'Günlük_Değişim',
       'Hisse_adet', 'Beta', '52 haftalık en yüksek fiyat',
       '52 haftalık en düşük fiyat']



 


"""  açılı menü """

hk=st.selectbox("Hisse seç", hkodu)


   
url[hk]=url[hk].fillna(method='ffill')
#1 yıllık 
fi_1=url[(url["Date"] >='2024-10-28') &(url['Date'] <='2025-10-24')]
ilkk=fi_1[hk].iloc[0]
sonn=fi_1[hk].iloc[-1]
fi_1_yüz=((sonn / ilkk) ** (1/1) - 1 )* 100
st.write(f"{hk}: {fi_1_yüz:.2f}%")
st.write(f"1yıllık getiri", fi_1_yüz * 1000)

   
   # 2 yıllık 
fi_2=url[(url['Date'] >="2023-10-28") & (url['Date'] <="2025-10-25")]
ilk_2=fi_2[hk].iloc[0]
son_2=fi_2[hk].iloc[-1]
fi_2_yüz=((son_2 / ilk_2) ** (1/2) - 1)* 100
st.write(f"{hk}: {fi_2_yüz:.2f}%")
st.write("2 yıllık getiri", fi_2_yüz * 1000)
# 3 yıllık
fi_3=url[(url['Date'] >="2022-10-28") & (url['Date'] <="2025-10-24")]
ilk_3=fi_3[hk].iloc[0]
son_3=fi_3[hk].iloc[-1]
fi_3_yüz=((son_3 / ilk_3) ** (1/3) -1 )*100
st.write(f"{hk}:{fi_3_yüz:.2f}%")
st.write("3 yıllık getiri", fi_3_yüz * 1000)
# 4 yıllık
fi_4=url[(url["Date"] >="2021-10-28") & (url['Date']  <="2025-10-24")]
ilk_4=fi_4[hk].iloc[0]
son_4=fi_4[hk].iloc[-1]
fi_4_yüz=((son_4 / ilk_4) ** (1/4) - 1 )*100
st.write(f"{hk}: {fi_4_yüz:.2f}%")
st.write("4 yıllık getiri", fi_4_yüz * 1000 )
# 5 yıllık 
fi_5 = url[(url['Date'] >= '2020-01-03') & (url['Date'] <= '2025-10-24')]
ilk=fi_5[hk].iloc[0] 
son=fi_5[hk].iloc[-1]

fi_5_yüz=((son / ilk) ** (1/5) - 1 )*100
st.write(f"{hk}: {fi_5_yüz:.2f}%")
st.write("5 yıllık getiri", fi_5_yüz * 1000)

fig, ax =plt.subplots()


sns.lineplot(x='Date' ,y=hk , data=url)
ax.set_title(f"{hk}  hissesinin 2020-2025 grafiği")
ax.set_xlabel=("Hisse")
ax.set_ylabel=("aa")
plt.grid(True)
st.pyplot(fig)


st.write(f"Hisse {hk}")
fig , ax=plt.subplots()
plt.bar(hıs_bılgı, hk)
ax.set_xlabel("Hisse")
ax.set_ylabel(hıs_bılgı)
st.pyplot(fig)


aa=url.corr()
gg=aa[(aa > 0.6) & (aa < 1)]

print(gg.stack())

