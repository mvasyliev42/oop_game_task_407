import logging
from telegram import Update, Bot
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler
import asyncio

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
async def send_message(bot_token, chat_id, text):
    bot = Bot(bot_token)
    await bot.send_message(chat_id=chat_id, text=text)

if __name__ == '__main__':
    #asyncio.run(send_message('5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw', 405301731, "tergfdg"))


    application = ApplicationBuilder().token('5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw').build()

    # bot = Bot('5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw')
    #
    # bot.send_message(chat_id=405301731, text="tergfdg")

    start_handler = CommandHandler('start', start)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()