from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
import os

TOKEN = os.getenv("BOT_TOKEN")

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton(
            "🎮 ဂိမ်းကစားရန်",
            url="https://www.365king.net"
        )
    ]
])

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://agp97.com/logo.png",
        caption="""👋 မင်္ဂလာပါ

🎮 အောက်က "ဂိမ်းကစားရန်" Button ကိုနှိပ်ပြီး ဝင်ကစားနိုင်ပါတယ်။
""",
        reply_markup=keyboard,
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot is running...")
app.run_polling()
