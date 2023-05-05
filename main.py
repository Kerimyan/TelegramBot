import os
from request_sender import RequestSender
from telegam_bot import CarFinderBot
from dotenv import load_dotenv
load_dotenv()

filename = 'cars.db'
if not os.path.exists(filename):
    sender = RequestSender(filename)
    for ind in range(2870005, 2915000):
        url = f"https://auto.am/offer/{ind}"
        sender.response_receiver(url)
else:
    API_KEY = os.getenv('API_KEY')
    bot = CarFinderBot(API_KEY)
    print('Bot is working now!!!')
    bot.start()
