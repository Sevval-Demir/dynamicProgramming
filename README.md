# ⚡ Enerji Duyarlı Algoritma Analizi

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![CodeCarbon](https://img.shields.io/badge/CodeCarbon-Sustainability-green)
![Status](https://img.shields.io/badge/Status-Educational-orange)

Bu proje, **dinamik programlama algoritmalarını** zaman, bellek ve özellikle **enerji karmaşıklığı** perspektifinden inceleyen akademik bir analiz çalışmasıdır.

Klasik algoritma analizine (Big-O) ek olarak, **enerji karmaşıklığı** kavramı hem **teorik modelleme** hem de **deneysel ölçümler** (CodeCarbon) aracılığıyla ele alınmıştır.  
Tüm deney süreci ve sonuçlar, **Streamlit tabanlı etkileşimli bir arayüz** üzerinden görselleştirilmektedir.

---

## 🎯 Projenin Amacı

Bu çalışma, algoritmaların performansını yalnızca hız (zaman) açısından değil, aynı zamanda **enerji tüketimi ve çevresel etki** açısından da değerlendirmeyi amaçlamaktadır:

1. **Teorik Modelleme:**  
   Enerji karmaşıklığını, zaman karmaşıklığı \(T(n)\) ile ilişkilendirerek teorik olarak modellemek  
   \(\;E(n) \propto T(n)\)

2. **Deneysel Gözlem:**  
   **CodeCarbon** kullanarak algoritmaların gerçek donanım üzerindeki karbon ayak izini ve enerji tüketimini ölçmek

3. **Karşılaştırmalı Analiz:**  
   Farklı girdi boyutlarında algoritmaların zaman, bellek ve enerji davranışlarını karşılaştırmak

4. **Yaklaşım Farkı:**  
   Grafik tabanlı ve tablo tabanlı dinamik programlama yaklaşımlarının enerji tüketim farklarını ortaya koymak

---

## 🧬 İncelenen Algoritmalar

| Algoritma | Tür | Açıklama |
|----------|-----|----------|
| **Bellman–Ford** | Graf Tabanlı | Tek kaynaklı en kısa yol algoritması. Negatif ağırlıklı kenarları destekler. |
| **Floyd–Warshall** | Graf Tabanlı | Tüm düğüm çiftleri için en kısa yolları hesaplar. |
| **0-1 Knapsack** | Tablo Tabanlı | **(Bonus)** Bellek erişimi yoğun, klasik dinamik programlama problemi. |

---

## 🔍 Ölçülen Metrikler

Projede hem teorik hem de donanım tabanlı metrikler kullanılmıştır.

### 1️⃣ Performans Metrikleri
- **Çalışma Süresi (T(n))**  
- **CPU Çalışma Süresi**  
- **Bellek Kullanımı (KB)**  

### 2️⃣ Enerji Metrikleri
- **Teorik Enerji Karmaşıklığı**  
  Ortalama güç tüketimi sabit kabul edilerek  
  \[
  E(n) \propto T(n)
  \]

- **Deneysel Enerji Tüketimi (CodeCarbon)**  
  Donanım sensörleri üzerinden ölçülen **CO₂ emisyonu (kg)**

- **Energy Impact Score (İkincil Metrik)**  
  \[
  \text{Time} \times \text{Memory}
  \]

> ⚠️ **Önemli:**  
> Teorik enerji karmaşıklığı ile CodeCarbon’dan elde edilen deneysel ölçümler **bilinçli olarak ayrı tutulmuştur**.  
> Teorik model algoritmanın yapısını, deneysel ölçüm ise gerçek sistem üzerindeki maliyeti temsil eder.

---

## 🧠 Akademik Yaklaşım ve Metodoloji

- Algoritmalar, arayüz ve dosya işlemlerinden (I/O) **izole edilerek** ölçülmüştür  
- Enerji karmaşıklığı, ders müfredatına ve literatüre uygun şekilde **zaman karmaşıklığına orantılı** modellenmiştir  
- Deney sonuçları, **tek seferlik ölçümler yerine tekrarlar üzerinden ortalama alınarak** hesaplanmıştır  
- 0-1 Knapsack algoritması, grafik tabanlı algoritmalardan farklı bir **bellek erişim modeli** sunduğu için bonus kapsamda eklenmiştir

---

## 🛠 Kullanılan Teknolojiler

- **Python 3.x**
- **Streamlit**
- **CodeCarbon**
- **psutil**
- **Pandas**
- **Matplotlib**

---

## 📂 Proje Yapısı

```text
dynamicProgramming/
├── algorithms/
│   ├── bellman_ford.py
│   ├── floyd_warshall.py
│   └── knapsack_01.py
├── experiments/
│   ├── run_bellman.py
│   ├── run_floyd.py
│   └── run_knapsack.py
├── measurements/
│   ├── time_tracker.py
│   ├── energy_tracker.py
│   └── codecarbon_tracker.py
├── results/
│   ├── csv/
│   │   └── results.csv
│   └── plots/
│       └── (otomatik üretilen grafikler)
├── app.py
└── requirements.txt
