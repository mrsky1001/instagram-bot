import os
import sys
import time

from instabot import Bot


def logout(bot):
    bot.logout()


def login(username, password):
    os.system('rm -rf config')
    bot = Bot()
    bot.login(username=username, password=password)
    time.sleep(2)
    return bot
