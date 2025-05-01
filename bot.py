from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7709876744:AAG_jh6IEuZm5MeRqYPt8raXYUtnrrO4F_0" 

#mensagens
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salve, FURIOSO(A)! 🔥\nBem-vindo ao bot da FURIA! \n\n\nAqui, você vai encontrar as últimas atualizações sobre nossos jogos, novidades da equipe, e tudo o que rola no mundo da FURIA! 🎮🔥\n\n\nJunte-se à FURIA e mostre seu apoio! Vamos juntos rumo à vitória! 🏆\n #GOFURIA")
async def quemSomos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Somos FURIA!\n\n Uma organização de esports que nasceu do desejo de representar o Brasil no CS e conquistou muito mais que isso: expandimos nossas ligas, disputamos os principais títulos, adotamos novos objetivos e ganhamos um propósito maior. Somos muito mais que o sucesso competitivo \n\n\n Somos um movimento sociocultural.")
#time
async def jogadores(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥TIME DE CS2🔥 \n MOLODOY\n YEKINDAR\n FalleN\n KSCERATO\n yuurih\n COACH: Hepa \n\n\nEsses são os nomes que carregam a camisa da FURIA com garra. Prepare-se para vibrar a cada round!")
#jogos
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Status ao vivo 🔥\n\n"
        "FURIA 11 x 8 NAVI — Mapa: Mirage\n"
        "Round 20 em andamento...\n"
        "KSCERATO acaba de levar dois na B!\n"
        "A torcida vai à loucura com a chance de fechar o mapa!")
async def proxjogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📅PRÓXIMO JOGO\n\n FURIA vs MIBR \n\n\n Data: 10/05 as 16:00 \n Contamos com a sua presença!!\n #GOFURIA")
#externos
async def redes (update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥REDES SOCIAIS🔥\n Instagram: @furiagg \n Youtube: youtube.com/FURIAgg\n X: @FURIA\n Tiktok: @furia  ")
async def loja (update:Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text("🔥LOJA DA FURIA🔥\n www.furia.gg")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("quemSomos", quemSomos))
    app.add_handler(CommandHandler("jogadores", jogadores))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("proxjogo", proxjogo))
    app.add_handler(CommandHandler("loja", loja))
    app.add_handler(CommandHandler("redes",redes))
    app.run_polling()