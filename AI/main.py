from telegram import Update, Bot, InputFile
from telegram.ext import filters, ApplicationBuilder, MessageHandler, ContextTypes, CommandHandler
import asyncio
from openai import OpenAI
import hashlib
import requests
from audioai import AudioAi


# Task 1
def set_url_to_file(prompt, url):
    with open('src/url_file.csv', 'a') as file_with_url:
        file_with_url.write(f'{prompt}|{url}\n')


def get_url_to_file(prompt):
    with open('src/url_file.csv') as file_to_read:
        for item in file_to_read.readlines():
            if item.startswith(prompt):
                return item.split('|')[1].strip()
    return False

# Task 2

def save_file(url):
    response = requests.get(url)
    file_name = md5_hash(url) + ".jpg"
    with open(f'src/{file_name}', 'wb') as file_to_open:
        file_to_open.write(response.content)
    return f'src/{file_name}'


def md5_hash(string):
    # Кодування рядка у байти
    encoded_string = string.encode()

    # Створення MD5 хешу
    md5_string = hashlib.md5(encoded_string)

    # Повернення хешу у шістнадцятковому форматі
    return md5_string.hexdigest()

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    client = OpenAI(api_key="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")

    url_result = get_url_to_file(update.message.text)
    if url_result:
        print(url_result)
        with open(url_result, 'rb') as file:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=InputFile(file))
    else:
        response = client.images.generate(
            model="dall-e-2",
            prompt=update.message.text,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        file_name = save_file(response.data[0].url)
        set_url_to_file(update.message.text, file_name)
        with open(file_name, 'rb') as file:
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=InputFile(file) )
    # todo: Чи є цей промт в файлі з посиланнями, якщо є, то віддаєм з файлу, якщо немає, то генеруємо

    # todo: зберегти цей файл

    # todo: Зберігаємо промпт з юрл адресою в файл



    #await context.bot.send_message(chat_id=update.effective_chat.id, text=response.data[0].url)
    ##photo = FileInpute()
    ##context.bot.send_photo()


# application = ApplicationBuilder().token('5732842940:AAERTmbxxw20fQniRntUkQ3m-ROPUS3t_xw').build()
#
# echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
# application.add_handler(echo_handler)
# application.run_polling()



audio_gen = AudioAi([
    "Ви, теж помітили, яка чудова весна цієї зими!"
])

for item in audio_gen:
    print(item)



