# SanDisk (SNDK) Hisse Senedi Fiyat Tahmini & Zaman Serisi Analizi

Bu proje, **SanDisk (SNDK)** hisse senedinin tarihsel fiyat hareketlerini analiz ederek, **AutoARIMA (Otoregresif Entegre Hareketli Ortalama)** zaman serisi modeli ile kısa vadeli (7 iş günü) fiyat projeksiyonu üretir ve sonuçları interaktif bir grafik üzerinde sunar.

---

## 📌 Proje Özeti

Finansal piyasalardaki volatilite ve trend analizlerini otomatikleştirmek amacıyla geliştirilen bu uygulamada;
1. **Yahoo Finance API** üzerinden son 2 yıla ait piyasa verileri çekilir.
2. **AutoARIMA** algoritması ile zaman serisine en uygun hiperparametreler ((p, d, q) değerleri) otomatik olarak optimize edilir.
3. Eğitilen model ile gelecek **7 iş günü** için kapanış fiyatı tahminleri hesaplanır.
4. **Plotly** kütüphanesi kullanılarak geçmiş 30 günlük gerçekleşen veriler ve gelecek tahminleri etkileşimli biçimde görselleştirilir.

---

## 🚀 Temel Özellikler

- **Otomatik Veri Çekme:** `yfinance` aracılığıyla güncel borsa verilerine hızlı erişim.
- **Otomatik Model Seçimi:** `pmdarima` ile manuel grid-search gerekmeksizin en düşük AIC/BIC skoruna sahip ARIMA modelinin tespiti.
- **İş Gününe Uyarlı Zamanlama:** Hafta sonu borsa kapalılıklarını gözeten iş günü (`freq='B'`) takvimi ile tarih hizalama.
- **İnteraktif Görselleştirme:** Yakınlaştırma (zoom), gezinme (pan) ve fare ile üzerine gelindiğinde değer inceleme (hover tooltip) imkânı sunan Plotly arayüzü.

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji / Kütüphane | Kullanım Amacı |
| :--- | :--- |
| **Python** | Temel programlama dili |
| **yfinance** | Finansal veri akışı ve borsa geçmişi edinimi |
| **pandas & numpy** | Zaman serisi manipülasyonu ve veri ön işleme |
| **pmdarima & statsmodels** | Otomatik ARIMA modelleme ve istatistiksel tahminleme |
| **Plotly** | İnteraktif veri görselleştirme |

---

## 📂 Proje Dizin Yapısı

```text
stock_arima_project/
│
├── app.py                      # Veri çekme, modelleme ve görselleştirme ana betiği
├── sandisk_stock_prices.csv    # Örnek/yerel veri seti yedeği
├── requirements.txt            # Proje bağımlılıkları listesi
└── README.md                   # Proje dokümantasyonu
```

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Depoyu Klonlayın veya İndirin
```bash
git clone https://github.com/kullanici_adi/stock_arima_project.git
cd stock_arima_project
```

### 2. Sanal Ortam Oluşturun ve Aktif Edin (Önerilen)
**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Uygulamayı Başlatın
```bash
python app.py
```

Betiği çalıştırdığınızda model eğitim adımları konsolda listelenecek ve ardından varsayılan tarayıcınızda interaktif tahmin grafiği açılacaktır.

---

## 📊 Örnek Çıktı ve Akış

```text
Performing stepwise search to minimize aic
 ARIMA(2,1,2)(0,0,0)[0] intercept   : AIC=...
 ARIMA(0,1,0)(0,0,0)[0] intercept   : AIC=...
 ...
Best model:  ARIMA(p,d,q)
```

Grafik üzerinde:
- 🔵 **Son 30 Gün:** Gerçekleşen piyasa kapanış fiyatları.
- 🔴 **Gelecek 7 Gün:** Model tarafından üretilen kesikli projeksiyon çizgisi ve hedef fiyat noktaları.

---

## ⚠️ Yasal Uyarı / Disclaimer

Bu proje yalnızca **eğitim, araştırma ve veri bilimi analitiği** amaçlarıyla geliştirilmiştir. Model tarafından üretilen tahminler **kesinlik içermez** ve herhangi bir şekilde **yatırım tavsiyesi (YTD)** niteliği taşımaz. Gerçek finansal kararlar alırken bağımsız profesyonel danışmanlık alınması önerilir.
