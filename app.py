import yfinance as yf
import pandas as pd
import warnings
import pmdarima as pm
import plotly.graph_objects as go

# sistemde ufak hatalar varsa gösterme
warnings.filterwarnings("ignore")

ticker = yf.Ticker("SNDK")

# son 2 yılı çek
history = ticker.history(period="2y")

# veriyi oluştur
df = pd.DataFrame(history)

df.index = df.index.tz_localize(None)

# df.to_csv('sandisk_stock_prices.csv')
# print("Dosya oluşturuldu.")

# print("\nTüm Yıllara Göre Hisse Tavan Fiyatı ve Tarihi:")
# print(int(df['High'].max()), '$')
# print(df['High'].idxmax())

# print("\nTüm Yıllara Göre Hisse Taban Fiyatı ve Tarihi:")
# print(int(df['Low'].min()), '$')
# print(df['Low'].idxmin())

# print("\nEksik Veri Var Mı?")
# print(df.isnull().sum())

# print("\nVeri Bilgisi:")
# print(df.info())

# print("\nTemel İstatistik Bilgileri:")
# print(df.describe())

# toplam = df["Volume"].sum()
# print(f'Toplam Alış/Satış Yapılan Hisse Sayısı:\n {toplam:,.3f} Adet')

# modeli eğitme
model_egit = pm.auto_arima(df['Close'],
                           seasonal=False,                           
                           trace=True,
                           error_action='ignore',
                           suppress_warnings=True,
                           stepwise=True)

# 126 gün, hafta sonları borsalar kapalı, 6 ay olarak ayarlandi
tahmin_adımı = 7
tahmin_sonuclari = model_egit.predict(n_periods=tahmin_adımı)

# gelecek 6 ay için tahmin
son_islem_tarihi = df.index[-1]
gelecek_tarihler = pd.date_range(start=son_islem_tarihi + pd.Timedelta(days=1), periods=tahmin_adımı, freq='B')
tahmin_sonuclari.index = gelecek_tarihler


tahmin_cizgisi = pd.concat([df['Close'].tail(1), tahmin_sonuclari])


fig = go.Figure()

# Geçmiş Veri
fig.add_trace(go.Scatter(
    x=df.index[-30:],
    y=df['Close'].tail(30),
    mode='lines+markers',
    name='Son 30 Gün',
    line=dict(color='blue', width=2),
    marker=dict(size=6)
))

# Tahmin Verisi
fig.add_trace(go.Scatter(
    x=tahmin_cizgisi.index,
    y=tahmin_cizgisi,
    mode='lines+markers',
    name='Gelecek 7 Gün',
    line=dict(color='red', width=2, dash='dash'),
    marker=dict(symbol='x', size=8)
))

# UI
fig.update_layout(
    title='Hisse Senedi Kısa Vadeli (7 Günlük) İnteraktif Fiyat Tahmini',
    xaxis_title='Tarih',
    yaxis_title='Kapanış Fiyatı ($)',
    template='plotly_white',
    hovermode='x unified',
    legend=dict(yanchor='top', y=0.99, xanchor='left', x=0.01)
)

fig.show()