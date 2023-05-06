import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
load_dotenv()
from database import Database


class CarFinderBot:
    def __init__(self, token, filename):
        self.filename = filename
        self.bot = telebot.TeleBot(token)

    def start(self):
        @self.bot.message_handler(commands=['start'])
        def start_command(message):
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            find_car_butten = KeyboardButton('/Search_Cars')
            keyboard.add(find_car_butten)

            self.bot.send_message(message.chat.id, "Hi. I'm car finder Bot... I can find cars from 'Auto.am'",
                                  reply_markup=keyboard)

        @self.bot.message_handler(commands=['Search_Cars'])
        def find_command(message):
            keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True)
            search_via_mark = KeyboardButton('/Search_Via_Mark')
            search_via_model = KeyboardButton('/Search_Via_Model')
            search_via_year = KeyboardButton('/Search_Via_Year')
            search_via_price = KeyboardButton('/Search_Via_Price')
            keyboard2.add(search_via_mark, search_via_model, search_via_year, search_via_price)

            self.bot.send_message(message.chat.id, "How do you want to perform the search?", reply_markup=keyboard2)

        @self.bot.message_handler(commands=['Search_Via_Mark'])
        def search_via_mark(message):
            self.search_tool = 'car_mark'
            self.bot.send_message(message.chat.id, "Enter the car mark you are looking for..")

            @self.bot.message_handler(func=lambda m: True)
            def handle_user_input(message):
                search_query = message.text
                db = Database(self.filename)
                results = db.search_value(self.search_tool, search_query)
                if results == []:
                    self.bot.reply_to(message, "No result!!!Try again...")
                else:
                    for result in results:
                        self.bot.send_message(message.chat.id,
                                              f'- {result[1]} {result[2]} {result[3]} \n'
                                              f'Price--${result[4]}\n' + f' {result[5]}' + '\n')

        @self.bot.message_handler(commands=['Search_Via_Model'])
        def search_via_mark(message):
            self.search_tool = 'car_model'
            self.bot.send_message(message.chat.id, "Enter the car model you are looking for..")

            @self.bot.message_handler(func=lambda m: True)
            def handle_user_input(message):
                search_query = message.text
                db = Database(self.filename)
                results = db.search_value(self.search_tool, search_query)
                if results == []:
                    self.bot.reply_to(message, "No result!!!Try again...")
                else:
                    for result in results:
                        self.bot.send_message(message.chat.id,
                                              f'- {result[1]} {result[2]} {result[3]} \n'
                                              f'Price--${result[4]}\n' + f' {result[5]}' + '\n')

        @self.bot.message_handler(commands=['Search_Via_Year'])
        def search_via_mark(message):
            self.search_tool = 'car_year'
            self.bot.send_message(message.chat.id, "Enter the car year you are looking for..")

            @self.bot.message_handler(func=lambda m: True)
            def handle_user_input(message):
                search_query = message.text
                db = Database(self.filename)
                results = db.search_value(self.search_tool, search_query)
                if results == []:
                    self.bot.reply_to(message, "No result!!!Try again...")
                else:
                    for result in results:
                        self.bot.send_message(message.chat.id,
                                              f'- {result[1]} {result[2]} {result[3]} \n'
                                              f'Price--${result[4]}\n' + f' {result[5]}' + '\n')

        @self.bot.message_handler(commands=['Search_Via_Price'])
        def search_via_mark(message):
            self.search_tool = 'car_price'
            self.bot.send_message(message.chat.id, "Enter the car price you are looking for..")

            @self.bot.message_handler(func=lambda m: True)
            def handle_user_input(message):
                search_query = message.text
                db = Database(self.filename)
                results = db.search_value(self.search_tool, search_query)
                if results == []:
                    self.bot.reply_to(message, "No result!!!Try again...")
                else:
                    for result in results:
                        self.bot.send_message(message.chat.id,
                                              f'- {result[1]} {result[2]} {result[3]} \n'
                                              f'Price--${result[4]}\n' + f' {result[5]}' + '\n')

        self.bot.polling()

