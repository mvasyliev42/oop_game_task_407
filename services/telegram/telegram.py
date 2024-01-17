import logging
from telegram import Update, Bot
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler
from time import sleep
# не викнується старт
class Telegram:

    def __init__(self) -> None:
        bot_token = '5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw'
        self.application = ApplicationBuilder().token(bot_token).build()
        self.start_handler = CommandHandler('start', Telegram.start)
        self.application.add_handler(self.start_handler)
        self.chat_id_p1 = False
        self.chat_id_p2 = False
        self.bot = Bot(bot_token)
        self.echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), self.action)
        self.message_p1 = False
        self.message_p2 = False
        self.application.add_handler(self.echo_handler)

    async def action(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
        if update.effective_chat.id == self.chat_id_p1:
            self.message_p1 = update.message.text
        if update.effective_chat.id == self.chat_id_p2:
            self.message_p2 = update.message.text
    
    def connectPlayer1(self):
        print("цикл виконується")
        while self.chat_id_p1 == False:
            sleep(1)


    def connectPlayer2(self):
        print("цикл виконується")
        while self.chat_id_p2 == False:
            sleep(1)

    async def start( update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("працюємо")
        if self.chat_id_p1 == False:
            self.chat_id_p1 = update.effective_chat.id
            await context.bot.send_message(chat_id=update.effective_chat.id, text="You are player 1")
        elif self.chat_id_p2 == False:
            self.chat_id_p2 = update.effective_chat.id
            await context.bot.send_message(chat_id=update.effective_chat.id, text="You are player 2")
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

    
    
    def sendMessagesPlayer1(self, messages):
        
        self.bot.send_message(chat_id=self.chat_id_p1, text=messages)

    def sendMessagesPlayer2(self, messages):
        
        self.bot.send_message(chat_id=self.chat_id_p2, text=messages)

    def recvMessagesPlayer1(self):
        while self.message_p1 == False:
            
            sleep(1)
        new_message_p1 = self.message_p1
        self.message_p1 = False
        return new_message_p1

    def recvMessagesPlayer2(self):
        while self.message_p2 == False:
            
            sleep(1)
        new_message_p2 = self.message_p1
        self.message_p2 = False
        return new_message_p2