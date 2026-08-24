import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import pmdarima as pm
import warnings
import io
from telegram.ext import Application, ContextTypes

# -- Bulut Sunucu için sahte websitesi eklentisi (keep-alive) ---
from flask import Flask
from threading import Thread

app_flask = Flask(__name__)
@app_flask.route('/')
def home():
    return "Bot 7/24 Bulutta Aktif Olarak Çalışıyor!"

def run():
    app_flask.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ----------------------------------------------------------

warnings.filterwarnings("ignore")


# kendi bilgilerin
TOKEN = "BURAYA_BOT_TOKENINI_YAZ"
CHAT_ID = "BURAYA_KENDI_CHAT_ID_NUMARANI_YAZ"
TAKIP_EDILEN_HISSE = "HİSSE_SENEDİ_ADI"
# ---------------------------

async def otomatik_rapor_hazirla(context: ContextTypes.DEFAULT_TYPE):
    ticker = TAKIP_EDILEN_HISSE
    try:
        print(f"[{ticker}] Raporu bulut üzerinden hazırlanıyor...")
        history = yf.Ticker(ticker).history(period="2y")
        if history.empty:
            print("Veri çekilemedi.")
            return

        df = pd.DataFrame(history)
        df.index = df.index.tz_localize(None)

        model_egit = pm.auto_arima(df['Close'], seasonal=False, trace=False, error_action='ignore', suppress_warnings=True, stepwise=True)
        tahmin_adimi = 7
        tahmin_sonuclari = model_egit.predict(n_periods=tahmin_adimi)

        gelecek_tarihler = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=tahmin_adimi, freq='B')
        tahmin_sonuclari.index = gelecek_tarihler
        tahmin_cizgisi = pd.concat([df["Close"].tail(1), tahmin_sonuclari])

        plt.figure(figsize=(10,5))
        plt.plot(df.index[-30:], df["Close"].tail(30), label='Son 30 Gün', color='blue', marker='o')
        plt.plot(tahmin_cizgisi.index, tahmin_cizgisi, label='Gelecek 7 Gün (Tahmin)', color='red', linestyle='--', marker='x')
        plt.title(f'{ticker} 7 Günlük Tahmin (Otomatik Rapor)')
        plt.xlabel('Tarih')
        plt.ylabel('Kapanış Fiyatı ($)')
        plt.legend()
        plt.grid(True)


        # resmi RAM'e kaydetme
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        plt.close()

        # resmi Telegram'a fotoğraf oalrak gönder
        await context.bot.send_photo(chat_id=CHAT_ID, photo=buf, caption=f"🚀 {ticker} Güncel Raporu!\nArka plan analiz sisteminiz bu raporu sizin için otomatik üretti.")
        print("✅ Rapor Telegram'a başarıyla gönderildi!")
    except Exception as Hata:
        print(f"❌ Hata: {str(Hata)}")

async def baslangic_gorevleri(application: Application):
    period = 10800 # 3 saat
    application.job_queue.run_repeating(otomatik_rapor_hazirla, interval=period, first=5)
    print("⏰ Zamanlayıcı kuruldu!")


if __name__ == '__main__':
    keep_alive() # flask sunucusunu arka planda başlatma (Render için)
    print("🚀 Borsa Kahini Başlatılıyor...")
    app = Application.builder().token(TOKEN).post_init(baslangic_gorevleri).build()
    app.run_polling()


