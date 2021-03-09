import sys
import time

import schedule

from strings import main_caption
from login_instabot import login

from posting_instabot import post_medias

username = sys.argv[1]
password = sys.argv[2]


def job_posting():
    print('job start')
    bot = login(username=username, password=password)
    try:
        post_medias(bot, './images', 3, main_caption)
        bot.logout()
    except BaseException as e:
        bot.logout()
        print(e)


schedule.every().day.at("06:35:00").do(job_posting)
schedule.every().day.at("13:27:00").do(job_posting)
schedule.every().day.at("18:22:00").do(job_posting)

print('Bot posting run.')
while True:
    schedule.run_pending()
    time.sleep(100)
