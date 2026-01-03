import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from google import genai
import os 

""" veri seti e tablo """
sheed_id="***************"
sheed_name="*****"
aa=f"https://docs.google.com/spreadsheets/d/{sheed_id}/gviz/tq?tqx=out:csv&sheet={sheed_name}"



url=pd.read_csv(aa)
url["fiyat"]=url["fiyat"].astype(str).str.replace(",",".")
url["fiyat"]=pd.to_numeric(url["fiyat"], errors="coerce")

print(url.columns)



st.write("merhaba pörtföy")

hk=["NVDA", "AAPL", "MSFT" , "AMZN", "GOOGL", "GOOG", "AVGO", "META", "TSLA"]

# anliz kısmı için
aaiz=["SPY","QQQ","DIA","IWM","VTI","IWM","IJH","XLK","XLF","XLV","XLE","XLY"]

gor_analiz=aaiz.copy()

port=st.multiselect("hisse seçiniz",hk)
pppört=[]
analiz=[]

tumu=port + aaiz
for myprfy in tumu:
    
    try:
        fıı=url.loc[url['Adı'] == myprfy, 'fiyat'].iloc[-1]
        adet=int(st.number_input(f"{myprfy} hissesi adetini giriniz:", min_value=0, key=f"adet_{myprfy}"))
        sektör=url.loc[url["Adı"]==myprfy, "sektör"].iloc[0]
        ppee=url.loc[url["Adı"]==myprfy , "pe_oranı"].iloc[0]
        ffor=url.loc[url["Adı"]==myprfy    ,"forward_pe"].iloc[0]
        kar=url.loc[url["Adı"]== myprfy, "kar_marjı"].iloc[0]
        eeps=url.loc[url["Adı"]==myprfy,"eps"].iloc[0]
        beta=url.loc[url["Adı"]==myprfy, "beta"].iloc[0]

        yıl_5=url.loc[url["Adı"]==myprfy, "5-yıl"].iloc[0] 
        yıl_1=url.loc[url["Adı"]==myprfy,"1-yıl"].iloc[0] 
        yıl_2=url.loc[url["Adı"]==myprfy,"2-yıl"].iloc[0] 
        yıl_3=url.loc[url["Adı"]==myprfy,"3-yıl"].iloc[0] 
        yıl_4=url.loc[url["Adı"]==myprfy,"4-yıl"].iloc[0] 

       

       
        h_degeri= adet * fıı
        pppört.append({
         "hisse":myprfy ,
         "adet":adet,
         "sektör": sektör,
         "fiyat": fıı,
         "değeri":h_degeri,
         "pe":ppee,
         "forward":ffor,
         "kar":kar,
         "eps":eeps,
         "beta":beta,
         "5_yıllık_getiri":yıl_5,
         "4_yıllık_getiri":yıl_4,
         "3_yıllık_getiri":yıl_3,
         "2_yıllık_getiri":yıl_2,
         "1_yıllık_getiri":yıl_1
      

    })
        
        # getiri
        analiz.append({
        "hisse":myprfy , 
        "5_yıllık_getiri":yıl_5,
        "4_yıllık_getiri":yıl_4,
        "3_yıllık_getiri":yıl_3,
        "2_yıllık_getiri":yıl_2,
        "1_yıllık_getiri":yıl_1,

             
             
             }) 
    
        
        


       

    except:
        fıı=0





    
   
my_p=pd.DataFrame(pppört)
st.dataframe(my_p)

# getiri
aa=pd.DataFrame(analiz)
st.dataframe(aa)



if st.button("oluştur"):
    # getiri   
    
    
    
    pörtföy= my_p["değeri"].sum()

    st.write(f"toplam değer: {pörtföy}")

    my_p["dağılım %"]=(my_p["değeri"] / pörtföy)*100
   
    
     # pasta grafiği dağılım
    fig, ax =plt.subplots()
    my_p=my_p.dropna(subset="dağılım %")
    ax.pie(my_p["dağılım %"], autopct="%1.1f%%" ,labels=my_p["hisse"])
    st.pyplot(fig)

    # forward_pe grafiği
    fig , ax=plt.subplots()
    ax.barh(my_p["hisse"] , my_p["eps"])
    ax.grid(True)
    st.pyplot(fig)

    fig , ax= plt.subplots()

    ax.barh(my_p["hisse"], my_p["forward"])
    st.pyplot(fig)




    
    #indirme bölümü 
    st.download_button("indir (excel)", my_p.to_csv(index=True) , "pörtföy.csv")


    st.balloons()

# chat bot bölümü

client=genai.Client(api_key="AIzaSyCjDe7IloE_Pvgtsj1h2vCL0PcpHMT838c")
    
sor=st.chat_input("sor:")
if sor:
  if sor.lower() in ["çık","out","bırak"]:
    st.stop()
        
  cevap=client.models.generate_content(
  model="gemini-2.0-flash",
  contents=sor
  )
  st.write("cevap:", cevap.text)
  st.caption("burdaki yazılanlar yatırım tavsiyesi değildir bilgileri kontrol ediniz !!!!")



