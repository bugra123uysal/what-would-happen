import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


""" veri seti e tablo """
sheed_id="1rpPfUqH85VJNk46apbkWYelprYiAPKw_"
sheed_name="ecl"
aa=f"https://docs.google.com/spreadsheets/d/{sheed_id}/gviz/tq?tqx=out:csv&sheet={sheed_name}"

url=pd.read_csv(aa)
url["fiyat"]=url["fiyat"].astype(str).str.replace(",",".")
url["fiyat"]=pd.to_numeric(url["fiyat"], errors="coerce")

print(url.columns)


st.write("merhaba pörtföy")

hk=["NVDA", "AAPL", "MSFT" , "AMZN", "GOOGL", "GOOG", "AVGO", "META", "TSLA",
     "LLY", "JPM", "WMT", "ORCL", "V", "XOM", "JNJ", "MA", "ABBV",
    "PLTR", "COST", "BAC", "AMD", "PG", "HD", "GE", "CVX", "UNH", "NFLX",
    "DIS", "KO", "PFE", "UNP", "TSM","MCD", "NKE", "SBUX", "CAT",
    "MMM", "MRK", "ABT", "LMT", "RTX", "GLW", "HON", "UPS"]


port=st.multiselect("hisse seçiniz",hk)
pppört=[]



for myprfy in port:

    
    
    try:
        fıı=url.loc[url['Adı'] == myprfy, 'fiyat'].iloc[-1]
        adet=int(st.number_input(f"{myprfy} hissesi adetini giriniz:", min_value=0))
        sektör=url.loc[url["Adı"]==myprfy, "sektör"].iloc[0] 
        
       
        h_degeri= adet * fıı
        pppört.append({
         "hisse":myprfy ,
         "adet":adet,
         "sektör": sektör,
         "fiyat": fıı,
         "değeri":h_degeri,
         

    })  

    except:
        fıı=0
    

   
my_p=pd.DataFrame(pppört)
st.dataframe(my_p)
if st.button("oluştur"):
    
   
   
    pörtföy= my_p["değeri"].sum()

    st.write(f"toplam değer: {pörtföy}")

    my_p["dağılım %"]=(my_p["değeri"] / pörtföy)*100

    st.dataframe(my_p)

    fig, ax =plt.subplots()
    ax.pie(my_p["dağılım %"], autopct="%1.1f%%" ,labels=my_p["hisse"] )
    
    st.pyplot(fig)


    fig, ax=plt.subplots()
    ax.plot(my_p.index, my_p["5-yıllık"] )
    ax.grid(True)
    st.pyplot(fig)



  
    
    st.balloons()

""" bileşik faiz hesaplama """

""" anapara """
ana_p=st.number_input("anapara",min_value=0)

""" vade süresi süre """
bekleme=st.number_input("vade süresi", min_value=0)
""" yüzde değişimi """
yze=[0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00]
yüzde=st.selectbox("yüzdesel değişimi şeçiniz: " ,yze)


if st.button("hesapla"): 
     bileşik_f=ana_p*(1 + yüzde) ** bekleme
     st.write("sonuç:",bileşik_f)

     st.balloons()

