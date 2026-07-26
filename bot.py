from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "7988055415:AAFkdfvOBJ42G9YEygxDBWVkxU2C4r85fRU"

async def chatbot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.text.lower()

    if user == "hello":
        await update.message.reply_text("Hello! Welcome to our Book Store.")

    elif user == "books":
        await update.message.reply_text("We have Python, Java, C, and HTML books.")

    elif user == "python":
        await update.message.reply_text("Python Crash Course - ₹599")

    elif user == "java":
        await update.message.reply_text("Head First Java - ₹699")

    elif user == "c":
        await update.message.reply_text("Let Us C - ₹499")

    elif user == "html":
        await update.message.reply_text("HTML & CSS - ₹399")

    elif user == "price":
        await update.message.reply_text("Prices range from ₹399 to ₹699.")

    elif user == "thanks":
        await update.message.reply_text("You're welcome! Visit again.")

    elif user == "bye":
        await update.message.reply_text("Thank you for visiting our Book Store!")

    else:
        await update.message.reply_text(
            "Sorry, I don't understand. Try: hello, books, python, java, c, html, price, thanks, bye"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.TEXT, chatbot))

print("Bot is running...")
app.run_polling()
