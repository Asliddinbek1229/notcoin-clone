from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackContext

BOT_TOKEN = '8235406826:AAG0eCcIGmh5sIRQec6lE9jAElK27vBkeRc'

async def start(update: Update, context: CallbackContext):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎮 Bosishni boshlash", web_app={"url": "https://notcoin-clone-eight.vercel.app/"})]
    ])
    await update.message.reply_text("Xush kelibsiz! Bosib ball oling👇", reply_markup=keyboard)

app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
