import requests
from car_finder import CarFinder
from database import Database


class RequestSender:
    def __init__(self, filename):
        self.database = Database(filename)
        self.database.create_table()

    def response_receiver(self, url):
        response = requests.get(url=url)
        if response.status_code != 404:
            self.data_saver(response, url)

    def data_saver(self, response, url):
        finder = CarFinder(response)
        self.database.insert_in_table(finder.get_mark(), finder.get_model(), finder.get_year(),
                                      finder.get_price(), url)
        print(30 * "==")



