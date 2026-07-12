from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = 972150268

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 مرحبًا!\n\nأرسل رسالتك، وسيتم إرسالها إلى صاحب البوت."
    )

async def forward(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = update.message.text or "[رسالة ليست نصية]"

    username = f"@{user.username}" if user.username else "لا يوجد"

    await context.bot.send_message(
        chat_id=OWNER_ID,
        text=f"""📩 رسالة جديدة

👤 الاسم: {user.full_name}
🔗 المعرف: {username}
🆔 ID: {user.id}

💬 الرسالة:
{text}
"""
    )

    await update.message.reply_text("✅ تم إرسال رسالتك بنجاح.")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.ALL, forward))

app.run_polling()
