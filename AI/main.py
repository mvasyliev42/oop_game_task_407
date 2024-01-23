from telegram import Update, Bot 
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler 
import asyncio
from openai import OpenAI






async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client = OpenAI(api_key="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")
    response = client.images.generate(
    model="dall-e-2",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
    )
    print(response.data[0].url)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response.data[0].url)
    ##photo = FileInpute()
    ##context.bot.send_photo()

application = ApplicationBuilder().token('5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw').build()

echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
application.add_handler(echo_handler)
application.run_polling()