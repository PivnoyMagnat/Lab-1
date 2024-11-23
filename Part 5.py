from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    menu_text = (
        "Доступні команди:\n"
        "/menu - показати це меню\n"
        "/whisper <текст> - повертає текст малими літерами\n"
        "/scream <текст> - повертає текст великими літерами"
    )
    await update.message.reply_text(menu_text)

async def whisper(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        whispered_text = ' '.join(context.args).lower()
        await update.message.reply_text(whispered_text)
    else:
        await update.message.reply_text("Будь ласка, додайте текст після команди /whisper")

async def scream(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        screamed_text = ' '.join(context.args).upper()
        await update.message.reply_text(screamed_text)
    else:
        await update.message.reply_text("Будь ласка, додайте текст після команди /scream")

def main():

    application = ApplicationBuilder().token("6231805377:AAHcpSFz3wm4CxIv1aU3DlKjPvSt3NqjGuQ").build()
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("whisper", whisper))
    application.add_handler(CommandHandler("scream", scream))

    print("Бот запущено. Натисніть Ctrl+C для завершення.")
    application.run_polling()
if __name__ == "__main__":
    main()