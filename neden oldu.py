import pandas as pd
import streamlit as st



""" veri seti e tablo """
sheed_id="*****"
sheed_name="**"
aa=f"https://docs.google.com/spreadsheets/d/{sheed_id}/gviz/tq?tqx=out:csv&sheet={sheed_name}"

url=pd.read_csv(aa)
url["fiyat"]=url["fiyat"].astype(str).str.replace(",",".")
url["fiyat"]=pd.to_numeric(url["fiyat"], errors="coerce")




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
       
        h_degeri= adet * fıı
        pppört.append({
         "hisse":myprfy ,
         "adet":adet,
         "fiyat": fıı,
         "değeri":h_degeri
    })  

    except:
        fıı=0
    

    
    
   
my_p=pd.DataFrame(pppört)
st.dataframe(my_p)
if st.button("oluştur"):
    
   
    pörtföy=0
    pörtföy+= my_p["değeri"].sum()
    st.write(f"toplam değer: {pörtföy}")
    st.balloons()


st.title("bileşik faiz hesaplama")


ana_p=st.number_input("anapara",min_value=0) # anapara hesaplama

 
bekleme=st.number_input("vade süresi", min_value=0) #vade süresi süre
""" yüzde değişimi """
yze=[0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1.00]
yüzde=st.selectbox("yüzdesel değişimi şeçiniz: " ,yze)


if st.button("hesapla"): 
     bileşik_f=ana_p*(1 + yüzde) ** bekleme
     st.write("sonuç:",bileşik_f)

     st.balloons()





 


    