# ⚡ Enerji Duyarlı Algoritma Analizi

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-App-red) ![CodeCarbon](https://img.shields.io/badge/CodeCarbon-Sustainability-green) ![Status](https://img.shields.io/badge/Status-Educational-orange)

Bu proje, **dinamik programlama algoritmalarını** zaman, bellek ve özellikle **enerji karmaşıklığı** perspektifinden inceleyen akademik bir analiz çalışmasıdır. Klasik algoritma analizine (Big-O) ek olarak, **enerji karmaşıklığı** kavramı hem **teorik modelleme** hem de **deneysel ölçümler** (CodeCarbon) aracılığıyla ele alınmıştır. Tüm deney süreci ve sonuçlar, **Streamlit tabanlı etkileşimli bir arayüz** üzerinden görselleştirilmektedir.

---

## 🎯 Projenin Amacı

Bu çalışma, algoritmaların performansını yalnızca hız (zaman) açısından değil, aynı zamanda **enerji tüketimi ve çevresel etki** açısından da değerlendirmeyi amaçlamaktadır:

1. **Teorik Modelleme:** Enerji karmaşıklığını, zaman karmaşıklığı T(n) ile ilişkilendirerek teorik olarak modellemek: E(n) ∝ T(n)
2. **Deneysel Gözlem:** **CodeCarbon** kullanarak algoritmaların gerçek donanım üzerindeki karbon ayak izini ve enerji tüketimini ölçmek
3. **Karşılaştırmalı Analiz:** Farklı girdi boyutlarında algoritmaların zaman, bellek ve enerji davranışlarını karşılaştırmak
4. **Yaklaşım Farkı:** Grafik tabanlı ve tablo tabanlı dinamik programlama yaklaşımlarının enerji tüketim farklarını ortaya koymak

---

## 🧬 İncelenen Algoritmalar

| Algoritma | Tür | Açıklama |
|-----------|-----|----------|
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
  Ortalama güç tüketimi sabit kabul edilerek: E(n) ∝ T(n)
  
- **Deneysel Enerji Tüketimi (CodeCarbon)**  
  Donanım sensörleri üzerinden ölçülen **CO₂ emisyonu (kg)**
  
- **Energy Impact Score (İkincil Metrik)**  
  Time × Memory

> ⚠️ **Önemli:**  
> Teorik enerji karmaşıklığı ile CodeCarbon'dan elde edilen deneysel ölçümler **bilinçli olarak ayrı tutulmuştur**.  
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
├── requirements.txt
└── README.md
```

---

## 🚀 Kurulum ve Çalıştırma

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin:

### 1️⃣ Projeyi Klonlayın

Öncelikle projeyi bilgisayarınıza indirin ve proje dizinine gidin:

```bash
git clone https://github.com/kullaniciadi/proje-adi.git
cd dynamicProgramming
```

### 2️⃣ Sanal Ortam (Virtual Environment) Oluşturun

```bash
# Sanal ortamı oluşturun
python -m venv venv

# Sanal ortamı aktif edin:
# Windows için:
venv\Scripts\activate

# Mac/Linux için:
source venv/bin/activate
```

### 3️⃣ Gerekli Paketleri Yükleyin

Proje için gerekli olan kütüphaneleri yükleyin:

```bash
pip install -r requirements.txt
```

### 4️⃣ Streamlit Uygulamasını Başlatın

```bash
streamlit run app.py
```

Tarayıcınızda otomatik olarak `http://localhost:8501` adresi açılacaktır.

---

## 📊 Kullanım

1. **Algoritma Seçimi:** Yan menüden analiz etmek istediğiniz algoritmayı seçin
2. **Girdi Boyutu:** Deney için girdi boyutunu belirleyin (örn: düğüm sayısı, kapasite)
3. **Deneyi Çalıştır:** "Run Experiment" butonuna tıklayın
4. **Sonuçları İnceleyin:** 
   - Zaman, bellek ve enerji grafikleri
   - Karbon ayak izi tabloları
   - Karşılaştırmalı analizler

---

## 📈 Örnek Sonuçlar

Proje, her deney sonucunda otomatik olarak şu verileri üretir:

- **CSV Formatında Ham Veri** (`results/csv/results.csv`)
- **Görselleştirme Grafikleri** (`results/plots/`)
  - Zaman karmaşıklığı grafikleri
  - Bellek kullanım grafikleri
  - Enerji tüketimi karşılaştırmaları
  - CO₂ emisyon analizleri

---

## 📈 Örnek Sonuçlar ve Görselleştirme

Proje çıktıları Streamlit arayüzünde interaktif grafiklere dönüştürülmektedir. Aşağıda Bellman-Ford, Floyd-Warshall ve Knapsack algoritmalarının karşılaştırmalı analizlerinden örnekler yer almaktadır.

### 📊 Performans Grafikleri

![Time Complexity](https://github.com/Sevval-Demir/dynamicProgramming/blob/main/results/plots/time_vs_vertices.png) 
![Energy Complexity](https://github.com/Sevval-Demir/dynamicProgramming/blob/main/results/plots/energy_complexity_vs_vertices.png)
![Experimental Energy Consumption](https://github.com/Sevval-Demir/dynamicProgramming/blob/main/results/plots/emissions_vs_vertices.png)
![Memory Analysis](https://github.com/Sevval-Demir/dynamicProgramming/blob/main/results/plots/memory_vs_vertices.png)


### 🗂️ Deneysel Veri Seti (CSV)

Deneyler sonucunda elde edilen ham verilerin bir kesiti aşağıdadır. Bu veriler `CodeCarbon` ve `psutil` kütüphaneleri kullanılarak toplanmıştır.

| Algorithm | Input Size | Time (s) | Memory (MB) | Energy (J) | CO2 Emissions (kg) |
|-----------|:----------:|:--------:|:-----------:|:----------:|:------------------:|
| **Bellman-Ford** | 100 | 0.0528 | 0.0469 | 0.0034 | 2.19e-07 |
| **Bellman-Ford** | 300 | 0.5236 | 0.1445 | 0.0412 | 2.76e-06 |
| **Floyd-Warshall** | 100 | 0.4852 | 0.2852 | 0.0423 | 2.68e-06 |
| **Floyd-Warshall** | 300 | 12.8941 | 1.8477 | 1.1542 | 6.83e-05 |
| **Knapsack** | 100 | 0.0003 | 0.0078 | 0.0012 | 8.54e-09 |
| **Knapsack** | 300 | 0.0007 | 0.0352 | 0.0013 | 9.06e-09 |

## 🔬 Teorik Arka Plan

### Enerji Karmaşıklığı Modeli

Algoritmaların enerji karmaşıklığı, zaman karmaşıklığı ile doğrudan ilişkilidir:

```
E(n) = P_avg × T(n)
```

Burada:
- **E(n):** Enerji karmaşıklığı
- **P_avg:** Ortalama güç tüketimi (sabit kabul edilir)
- **T(n):** Zaman karmaşıklığı

Bu model, algoritmanın teorik analizini enerji boyutuna genişletir.

### Algoritma Karmaşıklıkları

| Algoritma | Zaman Karmaşıklığı | Teorik Enerji | Alan Karmaşıklığı |
|-----------|-------------------|---------------|-------------------|
| **Bellman-Ford** | O(VE) | O(VE) | O(V) |
| **Floyd-Warshall** | O(V³) | O(V³) | O(V²) |
| **0-1 Knapsack** | O(nW) | O(nW) | O(nW) |

---

## ⚠️ Sınırlamalar ve Dikkat Edilmesi Gerekenler

1. **Donanım Bağımlılığı:** CodeCarbon ölçümleri, çalıştırılan donanıma göre değişiklik gösterir
2. **Arka Plan İşlemleri:** Deneyler sırasında diğer uygulamaları kapatmanız önerilir
3. **Küçük Girdi Boyutları:** Çok küçük girdilerde enerji ölçümleri gürültülü olabilir
4. **Platform Desteği:** CodeCarbon, tüm işlemcilerde aynı hassasiyette çalışmayabilir

---

## 🤝 Katkıda Bulunma

Bu proje açık kaynaklıdır ve katkılara açıktır. Katkıda bulunmak isterseniz:

1. Projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/yeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/yeniOzellik`)
5. Pull Request oluşturun

---

## 📝 Lisans

Bu proje eğitim amaçlıdır.

---

## 👥 İletişim

Sorularınız veya önerileriniz için:

- **GitHub Issues:** [Proje Sayfası](https://github.com/Sevval-Demir/dynamicProgramming.git)

---

## 🌟 Teşekkürler

Bu projeyi kullandığınız için teşekkür ederiz! Yıldız ⭐ vermeyi unutmayın.

---
