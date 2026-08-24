# Stock ARIMA Project - Hisse Senedi Fiyat Tahmini ve Telegram Botu

Bu proje, **SanDisk (SNDK)** veya belirlenen hisse senetlerinin geçmiş fiyat hareketlerini analiz ederek **AutoARIMA (Otoregresif Entegre Hareketli Ortalama)** modeliyle 7 iş günlük fiyat projeksiyonu üretir. Elde edilen tahminler hem yerel ortamda interaktif olarak incelenebilir hem de Telegram botu aracılığıyla periyodik olarak otomatik raporlanabilir.

---

## 📌 Özellikler

- **Otomatik Veri Çekme:** `yfinance` kullanılarak son 2 yıla ait borsa verileri alınır.
- **Otomatik Model Optimizasyonu:** `pmdarima` (AutoARIMA) ile seriye en uygun parametreler ((p, d, q)) otomatik belirlenir.
- **İş Günü Uyumlu Zamanlama:** Hafta sonlarını hariç tutan iş günü (`freq='B'`) takvimi ile gelecek 7 iş günü için kapanış fiyatı tahmini yapılır.
- **Telegram Botu ile Otomatik Raporlama (`app.py`):**
  - Arka planda `job_queue` zamanlayıcısı ile her 3 saatte bir otomatik çalışır.
  - Tahmin grafiğini Matplotlib ile bellek üzerinde (RAM / BytesIO) oluşturup doğrudan Telegram sohbetine fotoğraf olarak iletir.
- **Bulut / Keep-Alive Desteği (`app.py`):**
  - Flask web sunucusu (Port 8080) entegrasyonu sayesinde Render gibi bulut platformlarında 7/24 aktif kalabilir.
- **Yerel İnteraktif Analiz (`local_analiz.py`):**
  - Model eğitim adımlarını konsolda detaylı gösterir.
  - Plotly ile tarayıcıda yakınlaştırılabilir (zoom/pan) ve üzerine gelindiğinde değer gösteren interaktif grafik açar.

---

## 📂 Proje Yapısı

```text
stock_arima_project/
│
├── app.py                      # Telegram botu, Flask keep-alive ve otomatik zamanlanmış raporlama
├── local_analiz.py             # Yerel çalıştırma için Plotly destekli interaktif analiz betiği
├── sandisk_stock_prices.csv    # yfinance ile çekilen hisse senedi verisinin DataFrame hali
├── requirements.txt            # Proje bağımlılıkları listesi
└── README.md                   # Proje dokümantasyonu
```

---

## 🛠️ Kullanılan Teknolojiler

| Kütüphane / Araç | Kullanım Amacı |
| :--- | :--- |
| **Python** | Ana programlama dili |
| **yfinance** | Borsa geçmişi ve finansal veri çekimi |
| **pmdarima & statsmodels** | Otomatik ARIMA zaman serisi modelleme |
| **pandas & numpy** | Veri ön işleme ve zaman serisi manipülasyonu |
| **python-telegram-bot** | Telegram üzerinden otomatik mesaj ve grafik gönderimi |
| **matplotlib** | Telegram botu için grafik üretimi (BytesIO) |
| **plotly** | Yerel analiz için interaktif grafik görselleştirme |
| **Flask** | Bulut sunucularda keep-alive amacıyla çalışan hafif HTTP sunucusu |

---

## ⚙️ Kurulum ve Çalıştırma

### 1. Bağımlılıkları Yükleyin

```bash
pip install -r requirements.txt
```

---

### 2. Kullanım Seçenekleri

#### A. Telegram Botu ve Otomatik Raporlama Modu
`app.py` dosyasındaki Telegram ayarlarını (`TOKEN`, `CHAT_ID`, `TAKIP_EDILEN_HISSE`) kontrol edin veya güncelleyin:

```bash
python app.py
```
- Flask sunucusu arka planda başlar.
- Telegram botu devreye girer ve her 3 saatte bir belirlenen hissenin güncel tahmin grafiğini Telegram'a gönderir.

#### B. Yerel İnteraktif Analiz Modu
Sonuçları doğrudan yerel ortamda ve tarayıcınızda görmek için:

```bash
python local_analiz.py
```
- Konsolda ARIMA model arama adımlarını listeler.
- Varsayılan tarayıcınızda interaktif Plotly grafiğini açar.

---

## ⚠️ Yasal Uyarı

Bu projedeki analizler ve tahmin modelleri yalnızca **eğitim ve araştırma** amaçlıdır. Üretilen veriler kesinlik içermez ve **yatırım tavsiyesi (YTD)** niteliğinde değildir.
