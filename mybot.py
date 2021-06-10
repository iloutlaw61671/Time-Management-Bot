import telebot
from datetime import datetime
import pytz
from test import get_chat
#from timecheck import which_hour
TOKEN = '<BOT TOKEN>'
bot=telebot.TeleBot(TOKEN)

def sendMessage(chat_id,text):
    print("Sent")
    bot.send_message(chat_id, text)
    return()

def main():
    @bot.message_handler(commands=['Greet'])
    def greet(message):
        bot.reply_to(message,"Hey how's it going?")
        get_chat(message.chat.id)

    @bot.message_handler(commands=['timenow'])
    def timenow(message):
        now = datetime.now()
        tz = pytz.timezone('Asia/Kolkata')
        your_now = now.astimezone(tz)
        current_time = your_now.strftime("%H:%M:%S")
        bot.reply_to(message,current_time)
        #print(type(current_time)
    
    bot.polling()   

if __name__=='__main__':
    main()
