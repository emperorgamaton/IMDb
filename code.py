import os
import telebot
import imdb

my_secret = ....
bot = telebot.TeleBot(my_secret)

@bot.message_handler(func=lambda m: True)
def searchlibrary(message):
  ia = imdb.IMDb()
  name = message.text
  search = ia.search_movie(name)
  id = search[0].movieID
  series = ia.get_movie(id)
  rating = str(series.data['rating'])
  plot = str(series.data['plot'])
  response = ((search[0]['title']) + ": " + rating + '\n' + plot)
  bot.reply_to(message,response)
  

bot.polling()
