import os
import telebot
import random
import schedule
import time
from dotenv import load_dotenv
from _mysql.connection import connection, cursor

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot= telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def random_name() -> random:
    cursor.execute("SELECT name FROM status WHERE status = ''")
    data = cursor.fetchall()
    random_ = random.sample(data, 2)

    first = random_[0][0]
    second = random_[1][0]

    cursor.execute("INSERT INTO ready (name) VALUES (%s)", (first))
    cursor.execute("INSERT INTO ready (name) VALUES (%s)", (second))

    cursor.execute("SELECT name FROM ready WHERE name = %s OR name = %s", (first, second))
    ready_data = cursor.fetchall()

    cursor.execute("DELETE FROM status WHERE name = %s OR name = %s", (first, second))

    connection.commit()

    bot.send_message(1001173176, f'{ready_data[0][0]}\n{ready_data[1][0]}')