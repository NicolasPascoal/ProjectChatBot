from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7709876744:AAG_jh6IEuZm5MeRqYPt8raXYUtnrrO4F_0" 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salve, FURIOSO(A)! 🔥 Bem-vindo ao bot da FURIA!")

async def jogadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("TIME DE VALORANT🔥: \n Pryze, Khalil, Heat, Havoc\n TIME DE CS2🔥: \n FalleN, Kscerato, Yuurih, Skullz, Chelo")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("jogadores", jogadores))
    app.run_polling()
