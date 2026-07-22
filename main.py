import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import asyncio

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

BOT_TOKEN = "8691074289:AAG5-vZps9yM2vfbnO68AwyKKpARvfTi-sI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    
    keyboard = [
        [InlineKeyboardButton("🔘 অপশন ১", callback_data="1")],
        [InlineKeyboardButton("🔵 অপশন ২", callback_data="2")],
        [InlineKeyboardButton("🟢 অপশন ৩", callback_data="3")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"👋 হ্যালো {user.first_name}!\n\nএকটি অপশন বেছে নিন:",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    
    await query.answer()
    
    if query.data == "1":
        await query.edit_message_text(text="✅ আপনি অপশন ১ নির্বাচন করেছেন!")
    elif query.data == "2":
        await query.edit_message_text(text="✅ আপনি অপশন ২ নির্বাচন করেছেন!")
    elif query.data == "3":
        await query.edit_message_text(text="✅ আপনি অপশন ৩ নির্বাচন করেছেন!")

async def main() -> None:
    """Start the bot."""
    
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    
    print("=" * 50)
    print("✅ বট চালু হচ্ছে...")
    print("=" * 50)
    
    await application.initialize()
    await application.start()
    await application.updater.start_polling()
    
    print("✅ বট সফলভাবে চালু হয়েছে!")
    print("=" * 50)

if __name__ == '__main__':
    asyncio.run(main())
