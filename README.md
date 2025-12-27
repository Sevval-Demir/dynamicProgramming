# ⚡ Enerji Duyarlı Algoritma Analizi

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![CodeCarbon](https://img.shields.io/badge/CodeCarbon-Sustainability-green)
![Status](https://img.shields.io/badge/Status-Educational-orange)

Bu proje, **Dinamik Programlama** algoritmalarını zaman, bellek ve özellikle **enerji karmaşıklığı** perspektifinden inceleyen akademik bir analiz çalışmasıdır.

Klasik algoritma analizine (Big-O) ek olarak, **enerji karmaşıklığı** kavramı hem **teorik modelleme** hem de **deneysel ölçümler** (CodeCarbon) ile ele alınmıştır. Tüm süreç, **Streamlit** tabanlı etkileşimli bir arayüz üzerinden görselleştirilmektedir.

---

## 🎯 Projenin Amacı

Bu çalışma, algoritmaların performansını sadece hız (zaman) açısından değil, çevresel etki (enerji) açısından da değerlendirmeyi hedefler:

1.  **Teorik Modelleme:** Enerji karmaşıklığını, zaman karmaşıklığı ($T(n)$) ile ilişkilendirerek teorik olarak modellemek ($E(n) \propto T(n)$).
2.  **Deneysel Gözlem:** **CodeCarbon** kullanarak algoritmaların gerçek donanım üzerindeki karbon ayak izini ve güç tüketimini ölçmek.
3.  **Karşılaştırmalı Analiz:** Farklı girdi boyutlarında (n) algoritmaların davranışlarını kıyaslamak.
4.  **Yaklaşım Farkı:** Grafik tabanlı (Bellman-Ford, Floyd-Warshall) ve tablo tabanlı (Knapsack) dinamik programlama yaklaşımlarının enerji tüketim farklarını ortaya koymak.

---

## 🧬 İncelenen Algoritmalar

| Algoritma | Tür | Açıklama |
|-----------|-----|----------|
| **Bellman–Ford** | Graf Tabanlı | Tek kaynaklı en kısa yol (Single-Source Shortest Path). Negatif ağırlıklı kenarları yönetebilir. |
| **Floyd–Warshall** | Graf Tabanlı | Tüm çiftler için en kısa yol (All-Pairs Shortest Path). |
| **0-1 Knapsack** | Tablo Tabanlı | **(Bonus)** Bellek erişim yoğunluğu yüksek, klasik dinamik programlama örneği. |

---

## 🔍 Ölçülen Metrikler

Projede hem teorik hem de donanım tabanlı metrikler toplanmıştır:

### 1. Performans Metrikleri
* **Çalışma Süresi ($T(n)$):** Algoritmanın milisaniye cinsinden tamamlanma süresi.
* **CPU Süresi:** İşlemcinin aktif olarak kullanıldığı süre.
* **Bellek Kullanımı:** Anlık RAM tüketimi (KB).

### 2. Enerji Metrikleri
* **Teorik Enerji Karmaşıklığı:** Ortalama güç tüketimi sabit kabul edilerek, zaman karmaşıklığı üzerinden modellenen değer.
* **Deneysel Enerji Tüketimi (CodeCarbon):** Donanım sensörleri kullanılarak ölçülen $CO_2$ emisyonu (kg) ve güç tüketimi (kWh).
* **Energy Impact Score:** `Time × Memory` formülü ile türetilen, enerjiye duyarlı karşılaştırmayı destekleyen ikincil metrik.

> **⚠️ Önemli Not:** Teorik enerji karmaşıklığı (matematiksel model) ile CodeCarbon’dan elde edilen deneysel ölçümler **bilinçli olarak ayrı tutulmuştur**. Biri algoritmanın yapısını, diğeri donanım üzerindeki gerçek maliyetini temsil eder.

---

## 🧠 Akademik Yaklaşım ve Metodoloji

* **İzolasyon:** Algoritmalar, arayüz ve dosya işlemlerinden (I/O) yalıtılarak saf işlem süreleri ölçülmüştür.
* **Modelleme:** Enerji karmaşıklığı, ders müfredatına ve literatüre uygun olarak zaman karmaşıklığına orantılı modellenmiştir.
* **Veri Güvenilirliği:** Sonuçlar tek seferlik ölçümler yerine, belirlenen **tekrar sayısı (iterations)** üzerinden ortalama alınarak hesaplanmıştır.
* **Bonus Kapsam:** 0-1 Knapsack algoritması, graf algoritmalarından farklı bir bellek erişim modeline (tablo/matris) sahip olduğu için karşılaştırma grubuna eklenmiştir.

---

## 🛠 Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Arayüz:** Streamlit
* **Enerji Takibi:** CodeCarbon
* **Sistem İzleme:** psutil
* **Veri Analizi & Görselleştirme:** Pandas, Matplotlib

---

## 📂 Proje Yapısı

```text
dynamicProgramming/
├── algorithms/             # Algoritmaların saf implementasyonları
│   ├── bellman_ford.py
│   ├── floyd_warshall.py
│   └── knapsack_01.py
├── experiments/            # Deney koşucuları (Runner scripts)
│   ├── run_bellman.py
│   ├── run_floyd.py
│   └── run_knapsack.py
├── measurements/           # Ölçüm araçları (Decorator/Wrapper)
│   ├── time_tracker.py
│   ├── energy_tracker.py
│   └── codecarbon_tracker.py
├── results/                # Çıktı dizini
│   ├── csv/                # Ham veri (results.csv)
│   └── plots/              # Otomatik üretilen grafikler
├── app.py                  # Streamlit ana uygulaması
└── requirements.txt        # Bağımlılıklar

git clone [https://github.com/kullaniciadi/proje-adi.git](https://github.com/kullaniciadi/proje-adi.git)
cd dynamicProgramming

2️⃣ Sanal Ortam Oluşturun (Önerilen)
Bash

python -m venv venv
# Windows için:
venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate

Harika bir taslak hazırlamışsın. Projenin akademik ve teknik derinliğini ön plana çıkaracak, GitHub'da paylaştığında profesyonel bir portföy projesi gibi görünecek şekilde düzenledim.

Aşağıda, Markdown formatında kopyalayıp doğrudan kullanabileceğin düzenlenmiş versiyonu ve altında neleri neden değiştirdiğime dair kısa notları bulabilirsin.

📋 Kopyalanabilir README.md Dosyası
Markdown

# ⚡ Enerji Duyarlı Algoritma Analizi

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![CodeCarbon](https://img.shields.io/badge/CodeCarbon-Sustainability-green)
![Status](https://img.shields.io/badge/Status-Educational-orange)

Bu proje, **Dinamik Programlama** algoritmalarını zaman, bellek ve özellikle **enerji karmaşıklığı** perspektifinden inceleyen akademik bir analiz çalışmasıdır.

Klasik algoritma analizine (Big-O) ek olarak, **enerji karmaşıklığı** kavramı hem **teorik modelleme** hem de **deneysel ölçümler** (CodeCarbon) ile ele alınmıştır. Tüm süreç, **Streamlit** tabanlı etkileşimli bir arayüz üzerinden görselleştirilmektedir.

---

## 🎯 Projenin Amacı

Bu çalışma, algoritmaların performansını sadece hız (zaman) açısından değil, çevresel etki (enerji) açısından da değerlendirmeyi hedefler:

1.  **Teorik Modelleme:** Enerji karmaşıklığını, zaman karmaşıklığı ($T(n)$) ile ilişkilendirerek teorik olarak modellemek ($E(n) \propto T(n)$).
2.  **Deneysel Gözlem:** **CodeCarbon** kullanarak algoritmaların gerçek donanım üzerindeki karbon ayak izini ve güç tüketimini ölçmek.
3.  **Karşılaştırmalı Analiz:** Farklı girdi boyutlarında (n) algoritmaların davranışlarını kıyaslamak.
4.  **Yaklaşım Farkı:** Grafik tabanlı (Bellman-Ford, Floyd-Warshall) ve tablo tabanlı (Knapsack) dinamik programlama yaklaşımlarının enerji tüketim farklarını ortaya koymak.

---

## 🧬 İncelenen Algoritmalar

| Algoritma | Tür | Açıklama |
|-----------|-----|----------|
| **Bellman–Ford** | Graf Tabanlı | Tek kaynaklı en kısa yol (Single-Source Shortest Path). Negatif ağırlıklı kenarları yönetebilir. |
| **Floyd–Warshall** | Graf Tabanlı | Tüm çiftler için en kısa yol (All-Pairs Shortest Path). |
| **0-1 Knapsack** | Tablo Tabanlı | **(Bonus)** Bellek erişim yoğunluğu yüksek, klasik dinamik programlama örneği. |

---

## 🔍 Ölçülen Metrikler

Projede hem teorik hem de donanım tabanlı metrikler toplanmıştır:

### 1. Performans Metrikleri
* **Çalışma Süresi ($T(n)$):** Algoritmanın milisaniye cinsinden tamamlanma süresi.
* **CPU Süresi:** İşlemcinin aktif olarak kullanıldığı süre.
* **Bellek Kullanımı:** Anlık RAM tüketimi (KB).

### 2. Enerji Metrikleri
* **Teorik Enerji Karmaşıklığı:** Ortalama güç tüketimi sabit kabul edilerek, zaman karmaşıklığı üzerinden modellenen değer.
* **Deneysel Enerji Tüketimi (CodeCarbon):** Donanım sensörleri kullanılarak ölçülen $CO_2$ emisyonu (kg) ve güç tüketimi (kWh).
* **Energy Impact Score:** `Time × Memory` formülü ile türetilen, enerjiye duyarlı karşılaştırmayı destekleyen ikincil metrik.

> **⚠️ Önemli Not:** Teorik enerji karmaşıklığı (matematiksel model) ile CodeCarbon’dan elde edilen deneysel ölçümler **bilinçli olarak ayrı tutulmuştur**. Biri algoritmanın yapısını, diğeri donanım üzerindeki gerçek maliyetini temsil eder.

---

## 🧠 Akademik Yaklaşım ve Metodoloji

* **İzolasyon:** Algoritmalar, arayüz ve dosya işlemlerinden (I/O) yalıtılarak saf işlem süreleri ölçülmüştür.
* **Modelleme:** Enerji karmaşıklığı, ders müfredatına ve literatüre uygun olarak zaman karmaşıklığına orantılı modellenmiştir.
* **Veri Güvenilirliği:** Sonuçlar tek seferlik ölçümler yerine, belirlenen **tekrar sayısı (iterations)** üzerinden ortalama alınarak hesaplanmıştır.
* **Bonus Kapsam:** 0-1 Knapsack algoritması, graf algoritmalarından farklı bir bellek erişim modeline (tablo/matris) sahip olduğu için karşılaştırma grubuna eklenmiştir.

---

## 🛠 Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Arayüz:** Streamlit
* **Enerji Takibi:** CodeCarbon
* **Sistem İzleme:** psutil
* **Veri Analizi & Görselleştirme:** Pandas, Matplotlib

---

## 📂 Proje Yapısı

```text
dynamicProgramming/
├── algorithms/             # Algoritmaların saf implementasyonları
│   ├── bellman_ford.py
│   ├── floyd_warshall.py
│   └── knapsack_01.py
├── experiments/            # Deney koşucuları (Runner scripts)
│   ├── run_bellman.py
│   ├── run_floyd.py
│   └── run_knapsack.py
├── measurements/           # Ölçüm araçları (Decorator/Wrapper)
│   ├── time_tracker.py
│   ├── energy_tracker.py
│   └── codecarbon_tracker.py
├── results/                # Çıktı dizini
│   ├── csv/                # Ham veri (results.csv)
│   └── plots/              # Otomatik üretilen grafikler
├── app.py                  # Streamlit ana uygulaması
└── requirements.txt        # Bağımlılıklar
🚀 Kurulum ve Çalıştırma
1️⃣ Projeyi İndirin
Projeyi bilgisayarınıza klonlayın veya indirin:

Bash

git clone [https://github.com/kullaniciadi/proje-adi.git](https://github.com/kullaniciadi/proje-adi.git)
cd dynamicProgramming
2️⃣ Sanal Ortam Oluşturun (Önerilen)
Bash

python -m venv venv
# Windows için:
venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate
3️⃣ Gerekli Paketleri Yükleyin
Bash

pip install -r requirements.txt

Harika bir taslak hazırlamışsın. Projenin akademik ve teknik derinliğini ön plana çıkaracak, GitHub'da paylaştığında profesyonel bir portföy projesi gibi görünecek şekilde düzenledim.

Aşağıda, Markdown formatında kopyalayıp doğrudan kullanabileceğin düzenlenmiş versiyonu ve altında neleri neden değiştirdiğime dair kısa notları bulabilirsin.

📋 Kopyalanabilir README.md Dosyası
Markdown

# ⚡ Enerji Duyarlı Algoritma Analizi

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![CodeCarbon](https://img.shields.io/badge/CodeCarbon-Sustainability-green)
![Status](https://img.shields.io/badge/Status-Educational-orange)

Bu proje, **Dinamik Programlama** algoritmalarını zaman, bellek ve özellikle **enerji karmaşıklığı** perspektifinden inceleyen akademik bir analiz çalışmasıdır.

Klasik algoritma analizine (Big-O) ek olarak, **enerji karmaşıklığı** kavramı hem **teorik modelleme** hem de **deneysel ölçümler** (CodeCarbon) ile ele alınmıştır. Tüm süreç, **Streamlit** tabanlı etkileşimli bir arayüz üzerinden görselleştirilmektedir.

---

## 🎯 Projenin Amacı

Bu çalışma, algoritmaların performansını sadece hız (zaman) açısından değil, çevresel etki (enerji) açısından da değerlendirmeyi hedefler:

1.  **Teorik Modelleme:** Enerji karmaşıklığını, zaman karmaşıklığı ($T(n)$) ile ilişkilendirerek teorik olarak modellemek ($E(n) \propto T(n)$).
2.  **Deneysel Gözlem:** **CodeCarbon** kullanarak algoritmaların gerçek donanım üzerindeki karbon ayak izini ve güç tüketimini ölçmek.
3.  **Karşılaştırmalı Analiz:** Farklı girdi boyutlarında (n) algoritmaların davranışlarını kıyaslamak.
4.  **Yaklaşım Farkı:** Grafik tabanlı (Bellman-Ford, Floyd-Warshall) ve tablo tabanlı (Knapsack) dinamik programlama yaklaşımlarının enerji tüketim farklarını ortaya koymak.

---

## 🧬 İncelenen Algoritmalar

| Algoritma | Tür | Açıklama |
|-----------|-----|----------|
| **Bellman–Ford** | Graf Tabanlı | Tek kaynaklı en kısa yol (Single-Source Shortest Path). Negatif ağırlıklı kenarları yönetebilir. |
| **Floyd–Warshall** | Graf Tabanlı | Tüm çiftler için en kısa yol (All-Pairs Shortest Path). |
| **0-1 Knapsack** | Tablo Tabanlı | **(Bonus)** Bellek erişim yoğunluğu yüksek, klasik dinamik programlama örneği. |

---

## 🔍 Ölçülen Metrikler

Projede hem teorik hem de donanım tabanlı metrikler toplanmıştır:

### 1. Performans Metrikleri
* **Çalışma Süresi ($T(n)$):** Algoritmanın milisaniye cinsinden tamamlanma süresi.
* **CPU Süresi:** İşlemcinin aktif olarak kullanıldığı süre.
* **Bellek Kullanımı:** Anlık RAM tüketimi (KB).

### 2. Enerji Metrikleri
* **Teorik Enerji Karmaşıklığı:** Ortalama güç tüketimi sabit kabul edilerek, zaman karmaşıklığı üzerinden modellenen değer.
* **Deneysel Enerji Tüketimi (CodeCarbon):** Donanım sensörleri kullanılarak ölçülen $CO_2$ emisyonu (kg) ve güç tüketimi (kWh).
* **Energy Impact Score:** `Time × Memory` formülü ile türetilen, enerjiye duyarlı karşılaştırmayı destekleyen ikincil metrik.

> **⚠️ Önemli Not:** Teorik enerji karmaşıklığı (matematiksel model) ile CodeCarbon’dan elde edilen deneysel ölçümler **bilinçli olarak ayrı tutulmuştur**. Biri algoritmanın yapısını, diğeri donanım üzerindeki gerçek maliyetini temsil eder.

---

## 🧠 Akademik Yaklaşım ve Metodoloji

* **İzolasyon:** Algoritmalar, arayüz ve dosya işlemlerinden (I/O) yalıtılarak saf işlem süreleri ölçülmüştür.
* **Modelleme:** Enerji karmaşıklığı, ders müfredatına ve literatüre uygun olarak zaman karmaşıklığına orantılı modellenmiştir.
* **Veri Güvenilirliği:** Sonuçlar tek seferlik ölçümler yerine, belirlenen **tekrar sayısı (iterations)** üzerinden ortalama alınarak hesaplanmıştır.
* **Bonus Kapsam:** 0-1 Knapsack algoritması, graf algoritmalarından farklı bir bellek erişim modeline (tablo/matris) sahip olduğu için karşılaştırma grubuna eklenmiştir.

---

## 🛠 Kullanılan Teknolojiler

* **Dil:** Python 3.x
* **Arayüz:** Streamlit
* **Enerji Takibi:** CodeCarbon
* **Sistem İzleme:** psutil
* **Veri Analizi & Görselleştirme:** Pandas, Matplotlib

---

## 📂 Proje Yapısı

```text
dynamicProgramming/
├── algorithms/             # Algoritmaların saf implementasyonları
│   ├── bellman_ford.py
│   ├── floyd_warshall.py
│   └── knapsack_01.py
├── experiments/            # Deney koşucuları (Runner scripts)
│   ├── run_bellman.py
│   ├── run_floyd.py
│   └── run_knapsack.py
├── measurements/           # Ölçüm araçları (Decorator/Wrapper)
│   ├── time_tracker.py
│   ├── energy_tracker.py
│   └── codecarbon_tracker.py
├── results/                # Çıktı dizini
│   ├── csv/                # Ham veri (results.csv)
│   └── plots/              # Otomatik üretilen grafikler
├── app.py                  # Streamlit ana uygulaması
└── requirements.txt        # Bağımlılıklar
🚀 Kurulum ve Çalıştırma
1️⃣ Projeyi İndirin
Projeyi bilgisayarınıza klonlayın veya indirin:

Bash

git clone [https://github.com/kullaniciadi/proje-adi.git](https://github.com/kullaniciadi/proje-adi.git)
cd dynamicProgramming
2️⃣ Sanal Ortam Oluşturun (Önerilen)
Bash

python -m venv venv
# Windows için:
venv\Scripts\activate
# Mac/Linux için:
source venv/bin/activate
3️⃣ Gerekli Paketleri Yükleyin
Bash

pip install -r requirements.txt
4️⃣ Uygulamayı Başlatın
Streamlit arayüzünü ayağa kaldırmak için:

Bash

streamlit run app.py

🖥 Arayüz Kullanımı
Uygulama açıldığında sol panelden deney parametrelerini belirleyebilirsiniz:

Girdi Boyutu (Input Size):

Graf algoritmaları için: Düğüm (Vertex) sayısı.

Knapsack için: Eşya (Item) sayısı.

Kenar Yoğunluğu: Graf tabanlı algoritmalar için "Sparse" (Seyrek) veya "Dense" (Yoğun) graf seçimi.

Tekrar Sayısı: Sonuçların tutarlılığı için deneyin kaç kez tekrarlanacağı.

Çıktılar:

İşlem tamamlandığında grafikler (Zaman, Enerji, Bellek) anlık olarak ekrana çizilir.

Ham veriler results/csv/results.csv dosyasına, grafikler results/plots/ dizinine otomatik kaydedilir.

📜 Lisans
Bu proje, akademik eğitim ve araştırma amaçlı hazırlanmıştır.


---
