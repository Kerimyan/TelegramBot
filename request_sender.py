import requests
from car_finder import CarFinder
from database import Database

filename = 'cars.db'
database = Database(filename)
database.create_table()
for ind in range(2870005, 2915000):
    url = f"https://auto.am/offer/{ind}"

    response = requests.get(url=url)
    if response.status_code != 404:
        finder = CarFinder(response)
        database.insert_in_table(finder.get_mark(), finder.get_model(), finder.get_year(), finder.get_price(), url)

        print(30 * "==")

    else:
        continue
