from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7709876744:AAG_jh6IEuZm5MeRqYPt8raXYUtnrrO4F_0" 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salve, FURIOSO(A)! 🔥 Bem-vindo ao bot da FURIA!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()