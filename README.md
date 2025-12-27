# ⚡ Enerji Duyarlı Algoritma Analizi

Bu proje, **dinamik programlama algoritmalarını** zaman, bellek ve **enerji karmaşıklığı** bakış açılarıyla incelemeyi amaçlamaktadır.  
Klasik algoritma analizine ek olarak, **enerji karmaşıklığı** kavramı hem **teorik** hem de **deneysel** olarak ele alınmıştır.

Proje kapsamında incelenen algoritmalar:
- **Bellman–Ford Algoritması** (graf tabanlı, tek kaynaklı en kısa yol)
- **Floyd–Warshall Algoritması** (graf tabanlı, tüm çiftler için en kısa yol)
- **0-1 Knapsack Algoritması** (tablo tabanlı dinamik programlama – bonus)

Deneylerin çalıştırılması ve sonuçların incelenmesi için **Streamlit tabanlı etkileşimli bir arayüz** sunulmaktadır.

---

## 🎯 Projenin Amacı

- Algoritmaların **zaman karmaşıklığını (T(n))** deneysel olarak incelemek  
- Enerji karmaşıklığını, ders kapsamında verilen tanıma uygun biçimde **teorik olarak modellemek**  
- **CodeCarbon** kullanarak algoritmaların deneysel enerji tüketimini gözlemlemek  
- Farklı girdi boyutlarında algoritmaları **karşılaştırmalı olarak analiz etmek**  
- Grafik tabanlı ve tablo tabanlı dinamik programlama yaklaşımlarının **enerji davranışlarını karşılaştırmak**

---

## 🔍 Ölçülen Metrikler

Bu projede aşağıdaki metrikler ölçülmüş ve analiz edilmiştir:

- **Çalışma Süresi (T(n))**
- **CPU Çalışma Süresi**
- **Bellek Kullanımı (KB)**
- **Enerji Karmaşıklığı (Teorik)**  
  `E(n) ∝ T(n)`  
  (ortalama güç tüketimi sabit kabul edilmiştir)
- **Deneysel Enerji Tüketimi**  
  → CodeCarbon ile ölçülen **CO₂ emisyonu (kg)**
- **Energy Impact Score (ikincil metrik)**  
  `time × memory`  
  (enerjiye duyarlı karşılaştırmayı desteklemek amacıyla)

> ⚠️ Teorik enerji karmaşıklığı ile CodeCarbon’dan elde edilen deneysel enerji ölçümleri **bilinçli olarak ayrı tutulmuştur**.

---

## 🧠 Akademik Yaklaşım

- Enerji karmaşıklığı, ders kapsamında verilen tanıma uygun olarak **zaman karmaşıklığı üzerinden modellenmiştir**
- **CodeCarbon**, bu teorik modelin gerçek sistemlerdeki karşılığını **karşılaştırmalı olarak gözlemlemek** amacıyla kullanılmıştır
- Grafik üretimi, dosya yazma ve kullanıcı arayüzü işlemleri **enerji ölçümüne dahil edilmemiştir**
- Algoritmalar **izole biçimde** ölçülmüştür
- 0-1 Knapsack algoritması, **bellek erişim yoğunluğu yüksek** tablo tabanlı bir dinamik programlama örneği olarak bonus kapsamında projeye dahil edilmiştir

---

## 🛠 Kullanılan Teknolojiler

- Python
- Streamlit
- psutil
- CodeCarbon
- Pandas
- Matplotlib

---

## 📂 Proje Yapısı

dynamicProgramming/
├─ algorithms/
│ ├─ bellman_ford.py
│ ├─ floyd_warshall.py
│ └─ knapsack_01.py
│
├─ experiments/
│ ├─ run_bellman.py
│ ├─ run_floyd.py
│ └─ run_knapsack.py
│
├─ measurements/
│ ├─ time_tracker.py
│ ├─ energy_tracker.py
│ └─ codecarbon_tracker.py
│
├─ results/
│ ├─ csv/
│ │ └─ results.csv
│ └─ plots/
│ └─ plot_results.py
│
├─ app.py
└─ README.md

---

## 🚀 Kurulum ve Çalıştırma

### 1️⃣ Gerekli paketleri yükleyin

pip install -r requirements.txt


### 2️⃣ Streamlit arayüzünü başlatın

streamlit run app.py


---

🖥 Arayüz Kullanımı

Aşağıdaki parametreler belirlenir:

Girdi boyutu

Graf algoritmaları için: düğüm (vertex) sayısı

Knapsack için: eşya sayısı

Kenar yoğunluğu (yalnızca graf tabanlı algoritmalar için)

Deney tekrar sayısı

İlgili algoritma çalıştırılır

Üretilen grafikler incelenir:

Zaman karmaşıklığı

Enerji karmaşıklığı (teorik)

Deneysel enerji tüketimi (CodeCarbon)

Bellek kullanımı

Tüm sonuçlar otomatik olarak:

CSV dosyasına kaydedilir

Deney tekrarları üzerinden ortalama alınır

Grafikler ile görselleştirilir

📊 Üretilen Çıktılar

CSV Dosyası: results/csv/results.csv

Grafikler: results/plots/

Zaman – girdi boyutu

Enerji karmaşıklığı – girdi boyutu

Deneysel enerji (emisyon) – girdi boyutu

Bellek kullanımı – girdi boyutu

📌 Notlar

Energy Impact Score, ana enerji metriği değildir; destekleyici bir karşılaştırma ölçütüdür

CodeCarbon çıktıları, teorik enerji karmaşıklığını doğrudan temsil etmez, deneysel gözlem amacıyla kullanılmıştır

Grafikler ve metrikler akademik olarak savunulabilir şekilde tasarlanmıştır

Bu çalışma, ders projesi kapsamında hazırlanmış olup yayınlanabilirlik hedefi gözetilerek yapılandırılmıştır

📜 Lisans

Bu proje eğitim ve araştırma amaçlı hazırlanmıştır.

---


