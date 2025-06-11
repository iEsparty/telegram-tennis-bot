from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from config import TELEGRAM_TOKEN, THESPORTSDB_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎾 Bienvenido al bot de apuestas de tenis en vivo.")

async def tenis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"https://www.thesportsdb.com/api/v1/json/{THESPORTSDB_API_KEY}/eventspastleague.php?id=4464"
    response = requests.get(url)
    data = response.json()

    eventos = data.get("events", [])[:5]
    mensajes = []
    for ev in eventos:
        mensaje = f"{ev['strEvent']} | {ev['dateEvent']} - Resultado: {ev.get('intHomeScore')} - {ev.get('intAwayScore')}"
        mensajes.append(mensaje)

    await update.message.reply_text("\n".join(mensajes) or "No hay datos disponibles.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tenis", tenis))
    app.run_polling()
