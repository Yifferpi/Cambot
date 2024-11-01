#! /usr/bin/env python3

from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram import BotCommand
from picamera import PiCamera
from time import sleep
import os
import logging

# Load environment variables
if "TOKEN" not in os.environ:
        print("Please set the TOKEN environment variable.")
        exit(1)
TOKEN = os.getenv('TOKEN')
if "USERS" not in os.environ:
        print("No users specified. You might want to limit who can use this bot.")
        USERS = []
else:
        USERS = [user.strip() for user in os.getenv('USERS').split(',')]
        print("Loaded users: " + str(USERS))
if "IMAGE_PATH" not in os.environ:
        print("Please set the IMAGE_PATH environment variable.")
        exit(1)
PATH = os.getenv('IMAGE_PATH')

camera = PiCamera()
camera.resolution = (1024, 768)
camera.led = False

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)


def about(update, context):
    context.bot.send_message(
            chat_id=update.effective_chat.id, 
            text="Hi! I'm the Cambot.\n\
            I take pictures for you.")

def pic(update, context):
    camera.start_preview()
    sleep(2) # Camera warm-up time
    camera.capture(PATH+'foo.jpg')
    context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(PATH+'foo.jpg', 'rb'))
#collect all images in a folder and timestamp them.
#send message if too many pictures have been taken

start_handler = CommandHandler('about', about)
pic_handler = CommandHandler('pic', pic, Filters.user(username=USERS))
commands = [ \
        BotCommand('about', "Tell me about you."), \
        BotCommand('pic', "Take a picture")]

dispatcher.add_handler(start_handler)
dispatcher.add_handler(pic_handler)
dispatcher.bot.set_my_commands(commands)

updater.start_polling()



