#! /usr/bin/env python3

from telegram.ext import Updater
from telegram.ext import CommandHandler
from picamera import PiCamera
import logging


TOKEN="***REMOVED***"

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)


def start(update, context):
    context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="I'm a bot, please talk to me!")

def pic(update, context):
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    sleep(2) # Camera warm-up time
    camera.capture('foo.jpg')
    context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo='foo.jpg')


start_handler = CommandHandler('start', start)
pic_handler = CommandHandler('pic', pic)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(pic_handler)

updater.start_polling()



