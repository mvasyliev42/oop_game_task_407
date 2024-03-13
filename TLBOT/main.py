import logging
from telegram import Update, Bot
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler
from services.authorisation import Authorisation
import asyncio

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def rating(update: Update, context: ContextTypes.DEFAULT_TYPE):

    #todo: отримання рейтингу

    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def registration(update: Update, context: ContextTypes.DEFAULT_TYPE):

    #todo: реєстрація користувача
    print(update)
    data = update.message.text.split(" ")
    authorisation = Authorisation(data[1], data[2])
    reg = authorisation.registration()
    reg = list(reg)
    reg = map(str, reg)
    text = "Ви успішно зареєструвалися, ваші данні: "+ ";".join(reg)
    await context.bot.send_message(chat_id=update.effective_chat.id, text= text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

if __name__ == '__main__':
    #asyncio.run(send_message('5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw', 405301731, "tergfdg"))

    #https://t.me/assistantlessonbot
    application = ApplicationBuilder().token('5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw').build()


    ratting_handler = CommandHandler('rating', rating)
    regestration_handler = CommandHandler('registration', registration)

    #echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    application.add_handler(ratting_handler)
    application.add_handler(regestration_handler)
    #application.add_handler(echo_handler)

    application.run_polling()
