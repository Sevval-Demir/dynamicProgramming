# ⚡ Enerji Duyarlı Algoritma Analizi

Bu proje, **graf tabanlı dinamik programlama algoritmalarını** zaman, bellek ve **enerji bakış açısıyla** incelemeyi amaçlamaktadır.  
Klasik algoritma analizine ek olarak, enerji kavramı hem **teorik** hem de **deneysel** olarak ele alınmıştır.

İncelenen algoritmalar:
- **Bellman–Ford**
- **Floyd–Warshall**

Proje, deneyleri çalıştırmak ve sonuçları görselleştirmek için **Streamlit tabanlı etkileşimli bir arayüz** sunar.

---

## 🎯 Projenin Amacı

- Algoritmaların **zaman karmaşıklığını** incelemek  
- Enerji karmaşıklığını, derste verilen tanıma uygun şekilde **teorik olarak modellemek**  
- **CodeCarbon** kullanarak deneysel enerji tüketimini ölçmek  
- Algoritmaları artan girdi boyutlarında **karşılaştırmalı olarak analiz etmek**

---

## 🔍 Ölçülen Metrikler

- **Çalışma Süresi (T(n))**
- **Bellek Kullanımı (KB)**
- **Enerji Karmaşıklığı – Teorik**  
  → `E(n) ∝ T(n)`  
  (ortalama güç sabit kabul edilmiştir)
- **Deneysel Enerji Tüketimi**  
  → CodeCarbon ile ölçülen **CO₂ emisyonu (kg)**
- **Energy Impact Score (ikincil metrik)**  
  → `time × memory`  
  (enerjiye duyarlı karşılaştırma amacıyla)

> ⚠️ Teorik enerji karmaşıklığı ile CodeCarbon’dan elde edilen deneysel enerji ölçümü **bilinçli olarak ayrı tutulmuştur**.

---

## 🧠 Akademik Yaklaşım

- **Enerji karmaşıklığı**, ders kapsamında verilen tanıma uygun olarak **zaman karmaşıklığı üzerinden modellenmiştir**
- **CodeCarbon**, bu teorik modelin **gerçek sistemlerdeki karşılığını gözlemlemek** için kullanılmıştır
- Grafik üretimi, dosya yazımı ve arayüz işlemleri enerji ölçümüne **dahil edilmemiştir**
- Algoritmalar **izole şekilde** ölçülmüştür

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
│ └─ floyd_warshall.py
│
├─ experiments/
│ ├─ run_bellman.py
│ └─ run_floyd.py
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

## 🖥 Arayüz Kullanımı

1. Şunları belirleyin:
   - Düğüm (vertex) sayısı
   - Kenar yoğunluğu
   - Tekrar sayısı
2. İlgili algoritmayı çalıştırın
3. Aşağıdaki grafikleri inceleyin:
   - Zaman karmaşıklığı
   - Enerji karmaşıklığı (teorik)
   - Deneysel enerji tüketimi (CodeCarbon)
   - Bellek kullanımı

Tüm sonuçlar otomatik olarak:
- CSV dosyasına kaydedilir
- Tekrarlar üzerinden ortalama alınır
- Grafiklerle görselleştirilir

---

## 📊 Üretilen Çıktılar

- **CSV Dosyası:** `results/csv/results.csv`
- **Grafikler:** `results/plots/`
  - Zaman – düğüm sayısı
  - Enerji karmaşıklığı – düğüm sayısı
  - Deneysel enerji (emisyon) – düğüm sayısı
  - Bellek kullanımı – düğüm sayısı

---

## 📌 Notlar

- Energy Impact Score **ana enerji metriği değildir**
- CodeCarbon çıktıları **teorik enerji karmaşıklığını doğrulayıcı deneysel veri** olarak kullanılmıştır
- Grafik isimlendirmeleri ve yorumlar **akademik olarak savunulabilir** şekilde tasarlanmıştır

---

## 📜 Lisans

Bu proje **eğitim ve araştırma amaçlı** hazırlanmıştır.
