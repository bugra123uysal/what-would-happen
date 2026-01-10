import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from google import genai
import requests
import os 

""" veri seti e tablo """
sheed_id="*********"
sheed_name="********"
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

        if myprfy in aaiz:
             adet=1
             h_degeri=0
        else:
       
            adet=int(st.number_input(f"{myprfy} hissesi adetini giriniz:", min_value=0, key=f"adet_{myprfy}"))
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
    # portföy getirileri  
    portfoy_getirisi_1=((my_p["değeri"] * aa["1_yıllık_getiri"]).sum() / my_p["değeri"].sum())
    portfoy_getirisi_2=((my_p["değeri"] * aa["2_yıllık_getiri"]).sum() / my_p["değeri"].sum())
    portfoy_getirisi_3=((my_p["değeri"] * aa["3_yıllık_getiri"]).sum() / my_p["değeri"].sum())
    portfoy_getirisi_4=((my_p["değeri"] * aa["4_yıllık_getiri"]).sum() / my_p["değeri"].sum())
    portfoy_getirisi_5=((my_p["değeri"] * aa["5_yıllık_getiri"]).sum() / my_p["değeri"].sum())
    aaiz=["SPY","QQQ","DIA","IWM","VTI","IJH","XLK","XLF","XLV","XLE","XLY"]
   
   
    # 1 yıllık getiri
    # 1 yıllık analiz için karşılaştırma 
    geçti_1= aa[aa["1_yıllık_getiri"] > portfoy_getirisi_1]

    adet_1=len(geçti_1)

    st.write(f"portföy getirisi 1 yılda { portfoy_getirisi_1:.2f} getiri sağlamışdır  portföy getirisini {adet_1} tane geçen yatırım vardır o da {geçti_1["hisse"].tolist()} yatırımıdır")
    fig, ax=plt.subplots()
    ax.set_title("1 yıllık getiri")
    ax.barh(my_p["hisse"], aa["1_yıllık_getiri"])
    ax.axvline(portfoy_getirisi_1 , linestyle="--", color="red" ,label="portföy_getirisi")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)


    # 2 yıllık getiri
    geçti_2= aa[aa["2_yıllık_getiri"] > portfoy_getirisi_2]
    adet_2=len(geçti_2)




    st.write(f"portföy getirisi 2 yılda {portfoy_getirisi_2} getiri sağlamışdır portföy getirisi {adet_2} tane geçen yatırım vardır o da {geçti_2["hisse"].tolist()} yatırımıdır  ")
    fig , ax=plt.subplots()
    ax.set_title("2 yıllık getiri")
    ax.barh(my_p["hisse"], aa["2_yıllık_getiri"])
    ax.axvline(portfoy_getirisi_2 , linestyle="--" , color="red" ,label="portföy getirisi")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    # 3 yıllık getiri
    geçti_3=aa[aa["3_yıllık_getiri"] > portfoy_getirisi_3]
    adet_3=len(geçti_3)

    st.write(f"portföy getirisi 3 yılda {portfoy_getirisi_3} getiri sağlamışdır  {adet_3} tane geçen  yatırım vardır o da {geçti_3["hisse"].tolist()} yatırımıdır")
    fig , ax=plt.subplots()
    ax.set_title("3 yıllık getiri")
    ax.barh(my_p["hisse"], aa["3_yıllık_getiri"])
    ax.set_title("3 yıllık getiri")
    ax.axvline(portfoy_getirisi_3 , linestyle="--", color="red" , label="portföy getirisi")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
 
    # 4 yıllık getiri
    geçti_4=aa[aa["4_yıllık_getiri"] > portfoy_getirisi_4]
    adet_4=len(geçti_4)

    st.write(f"portföy getirisi 4 yılda {portfoy_getirisi_4} getiri sağlamışdır  {adet_4} tane  geçen yatırım vardır o da {geçti_4["hisse"].tolist()} yatırımıdır ")

    fig , ax=plt.subplots()
    ax.set_title("4 yıllık getiri")
    ax.barh(my_p["hisse"], aa["4_yıllık_getiri"])
    ax.axvline(portfoy_getirisi_4 , linestyle="--", color="red" ,label="portföy getirisi")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
 
# 5 yıllık getiri
    geçti_5=aa[aa["5_yıllık_getiri"] > portfoy_getirisi_5]
    adet_5=len(geçti_5)

    
    st.write(f"portföy getirisi 5 yılda {portfoy_getirisi_5} getiri sağladı {adet_5} tane  geçen yatırım vardır o da {geçti_4["hisse"].tolist()} yatırımıdır")

    fig , ax=plt.subplots()
    ax.set_title("5 yıllık getiri")
    ax.barh(my_p["hisse"], aa["5_yıllık_getiri"])
    ax.axvline(portfoy_getirisi_5 , linestyle="--", color="red" , label="portföy getirisi")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
 
    
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
