import logging
from telegram import Update, Bot
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler
from time import sleep

class Telegram:

    def __init__(self) -> None:
        bot_token = '5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw'
        self.application = ApplicationBuilder().token(bot_token).build()
        self.start_handler = CommandHandler('start', self.start)
        self.application.add_handler(self.start_handler)
        self.chat_id_p1 = False
        self.chat_id_p2 = False
        self.bot = Bot(bot_token)

    def connectPlayer1(self):
        while self.chat_id_p1 == False:
            sleep(1)


    def connectPlayer2(self):
        while self.chat_id_p2 == False:
            sleep(1)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        if self.chat_id_p1 == False:
            self.chat_id_p1 = update.update.effective_chat.id
            await context.bot.send_message(chat_id=update.effective_chat.id, text="You are player 1")
        elif self.chat_id_p2 == False:
            self.chat_id_p2 = update.update.effective_chat.id
            await context.bot.send_message(chat_id=update.effective_chat.id, text="You are player 2")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    
    
    
    def sendMessagesPlayer1(self, messages):
        
        self.bot.send_message(chat_id=self.chat_id_p1, text=messages)

    def sendMessagesPlayer2(self, messages):
        
        self.bot.send_message(chat_id=self.chat_id_p2, text=messages)