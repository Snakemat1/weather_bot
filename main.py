
import asyncio
import os
import requests


from telebot.async_telebot import AsyncTeleBot
from dotenv import load_dotenv

# env
load_dotenv()
# TOKEN = YOUR TOKEN
bot = AsyncTeleBot(os.getenv("TOKEN"))


# command = /your commands
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    
    await bot.reply_to(message, text)





@bot.message_handler(commands=['temperature'])
async def how_your_country(message):
    text = 'Please enter your region'
    await bot.reply_to(message,text)


@bot.message_handler()
async def counry(message):
    country = message.text
    url = "http://api.weatherapi.com/v1/current.json?key=7114732d6a1b4d53be9182107241605&q="  #api
    response = requests.get(url + country)  #select location
    await bot.reply_to(message,response.json()['current']['temp_c'])









asyncio.run(bot.polling())  #polling