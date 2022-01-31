from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from time import sleep
def start(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id, text='стартуем')

    context.bot.send_message(chat_id=user_id, text='Работаем')
    while 467657!= 997836793:
        context.bot.send_message(chat_id=user_id, text='Ебашим')
        sleep(1800)
 def star(update, context):
    user_id = update.message.chat_id
    context.bot.send_message(chat_id=user_id, text='стартуем')

    context.bot.send_message(chat_id=user_id, text='Работаем')
      
TOKEN ='5088514755:AAHh705K_7aQ65Ic1yPkGm23osNmlrmi_V4'
upd = Updater(token=TOKEN, workers=4)
dis = upd.dispatcher
dis.add_handler(CommandHandler(command='start', callback=start))
dis.add_handler(CommandHandler(command='star', callback=star))
upd.start_polling(drop_pending_updates=True)
