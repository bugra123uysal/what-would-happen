# 📊 Portfolio What-If


<img width="676" height="384" alt="Ekran görüntüsü 2025-12-13 225540" src="https://github.com/user-attachments/assets/bb58c678-1631-42b3-acf0-18277596ad20" />

#portfolio

<img width="687" height="332" alt="Ekran görüntüsü 2025-12-13 225135" src="https://github.com/user-attachments/assets/dba55a71-d1c6-4416-9459-43258879d70c" />



<img width="896" height="743" alt="Ekran görüntüsü 2026-01-11 005822" src="https://github.com/user-attachments/assets/74f2c415-a1ab-4548-823f-32adc7c9acb7" />


<img width="1917" height="712" alt="Ekran görüntüsü 2026-01-04 002537" src="https://github.com/user-attachments/assets/884e716b-f081-43dd-8c16-ab1ee4204179" />

 # getiriler


<img width="895" height="631" alt="Ekran görüntüsü 2026-01-11 005739" src="https://github.com/user-attachments/assets/d2e47a33-50ce-45b0-8736-dc797dd26b2a" />


<img width="857" height="630" alt="Ekran görüntüsü 2026-01-11 005748" src="https://github.com/user-attachments/assets/58a7525f-c5d8-44f8-abb7-b2b30a7f62b3" />


<img width="868" height="634" alt="Ekran görüntüsü 2026-01-11 005756" src="https://github.com/user-attachments/assets/d3d26b3f-dd34-4f72-9ca2-7bc6c1eefe30" />

<img width="861" height="632" alt="Ekran görüntüsü 2026-01-11 005804" src="https://github.com/user-attachments/assets/1ac5bc0a-6a16-4bfa-b9ba-830baf34a5af" />


<img width="948" height="631" alt="Ekran görüntüsü 2026-01-11 005812" src="https://github.com/user-attachments/assets/dda497fe-aa95-4846-8284-bb47170c6c8d" />


<img width="1352" height="783" alt="Ekran görüntüsü 2026-01-21 232641" src="https://github.com/user-attachments/assets/c26099b5-6ea3-4201-aa09-a5a2605b3c2d" />


**English** | [Türkçe](#-türkçe)

An experimental finance simulation tool that lets users build investment portfolios **without risking real money**, compare them against major indices and ETFs, and analyze the results through interactive visualizations.

> ⚠️ This is **not** an investment product and does **not** provide financial advice. The goal is to build a foundation for working with market data: fetching, comparing, and visualizing.

## 🎯 Purpose

- Build hypothetical portfolios from real market data
- Compare custom strategies against benchmarks (SPY, QQQ, DIA, sector ETFs, and more)
- See the results clearly through charts — no real trades, no real risk

## 🔄 Data Pipeline

The data flow is intentionally two-staged, prioritizing control and learning over full automation:

1. **Fetch** — Stock and index data is pulled via [yfinance](https://github.com/ranaroussi/yfinance)
2. **Store** — Data is written to Google Sheets
3. **Serve** — The Streamlit app reads the data through the Google Sheets CSV endpoint

This is a semi-automated pipeline by design: the priority at this stage is data discipline, not real-time speed.

## 🛠️ Features

**Portfolio & Strategy Builder**
- Select stocks and enter share counts
- Per-position value and total portfolio value are computed from current prices

**Fundamental Metrics** (per stock)
- EPS, Forward P/E, Beta, profit margin
- 1–5 year historical returns

**Visual Comparisons**
- Portfolio allocation (pie chart)
- Compound return comparison
- EPS / Forward P/E / annual return comparisons *(in progress)*

**AI Chatbot** *(experimental)*
- Gemini API integration for portfolio Q&A — early stage, accuracy not guaranteed

## 📸 Screenshots

### Compound Return
<img width="676" alt="Compound return comparison" src="https://github.com/user-attachments/assets/bb58c678-1631-42b3-acf0-18277596ad20" />

### Portfolio View
<img width="687" alt="Portfolio allocation" src="https://github.com/user-attachments/assets/dba55a71-d1c6-4416-9459-43258879d70c" />
<img width="896" alt="Portfolio detail" src="https://github.com/user-attachments/assets/74f2c415-a1ab-4548-823f-32adc7c9acb7" />
<img width="1917" alt="Full dashboard view" src="https://github.com/user-attachments/assets/884e716b-f081-43dd-8c16-ab1ee4204179" />

### Returns Analysis
<img width="895" alt="Returns comparison 1" src="https://github.com/user-attachments/assets/d2e47a33-50ce-45b0-8736-dc797dd26b2a" />
<img width="857" alt="Returns comparison 2" src="https://github.com/user-attachments/assets/58a7525f-c5d8-44f8-abb7-b2b30a7f62b3" />
<img width="868" alt="Returns comparison 3" src="https://github.com/user-attachments/assets/d3d26b3f-dd34-4f72-9ca2-7bc6c1eefe30" />
<img width="861" alt="Returns comparison 4" src="https://github.com/user-attachments/assets/1ac5bc0a-6a16-4bfa-b9ba-830baf34a5af" />
<img width="948" alt="Returns comparison 5" src="https://github.com/user-attachments/assets/dda497fe-aa95-4846-8284-bb47170c6c8d" />
<img width="1352" alt="Extended analysis" src="https://github.com/user-attachments/assets/c26099b5-6ea3-4201-aa09-a5a2605b3c2d" />

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| Data source | yfinance (Yahoo Finance) |
| Data storage | Google Sheets (CSV endpoint) |
| Analysis | pandas, matplotlib |
| AI (experimental) | Gemini API |

## ⚠️ Disclaimer

This project is for **educational purposes only**. It does not execute real trades, does not provide investment advice, and offers no guarantee of financial accuracy.

---

# 🇹🇷 Türkçe

Kullanıcıların **gerçek para riske etmeden** yatırım portföyleri oluşturabildiği, bu portföyleri büyük endeks ve ETF'lerle karşılaştırabildiği ve sonuçları interaktif grafiklerle analiz edebildiği deneysel bir finans simülasyon aracıdır.

> ⚠️ Bu proje bir yatırım ürünü **değildir** ve yatırım tavsiyesi **vermez**. Amaç, piyasa verisiyle çalışma altyapısı kurmaktır: veri çekme, karşılaştırma ve görselleştirme.

## 🎯 Amaç

- Gerçek piyasa verisiyle hipotetik portföyler oluşturmak
- Kendi stratejini benchmark'larla (SPY, QQQ, DIA, sektör ETF'leri vb.) karşılaştırmak
- Sonuçları grafiklerle net görmek — gerçek alım-satım yok, gerçek risk yok

## 🔄 Veri Akışı

Veri akışı bilinçli olarak iki aşamalıdır; bu aşamada öncelik gerçek zamanlılık değil, veri disiplinidir:

1. **Çekme** — Hisse ve endeks verileri [yfinance](https://github.com/ranaroussi/yfinance) ile çekilir
2. **Depolama** — Veriler Google Sheets'e aktarılır
3. **Okuma** — Streamlit uygulaması veriyi Google Sheets CSV endpoint'i üzerinden okur

## 🛠️ Özellikler

**Portföy ve Strateji Oluşturma**
- Hisse seç, adet gir
- Pozisyon değeri ve toplam portföy değeri güncel fiyatlardan hesaplanır

**Temel Finansal Metrikler** (hisse başına)
- EPS, Forward F/K, Beta, kâr marjı
- 1–5 yıllık geçmiş getiriler

**Görsel Karşılaştırmalar**
- Portföy dağılımı (pasta grafiği)
- Bileşik getiri karşılaştırması
- EPS / Forward F/K / yıllık getiri karşılaştırmaları *(geliştirme aşamasında)*

**AI Chatbot** *(deneysel)*
- Gemini API entegrasyonu — erken aşama, finansal doğruluk garanti edilmez

## ⚠️ Uyarı

Bu proje yalnızca **eğitim amaçlıdır**. Gerçek emir göndermez, yatırım tavsiyesi vermez ve finansal doğruluk garantisi sunmaz.

---

## 👤 Developer / Geliştirici

**Mesut Buğra Uysal**
[GitHub](https://github.com/bugra123uysal) · [LinkedIn](https://www.linkedin.com/in/mesut-bu%C4%9Fra-uysal-16a1bb288/)



Linkedin:https://www.linkedin.com/in/mesut-bu%C4%9Fra-uysal-16a1bb288/
