import sqlite3

from query import Query


class Database:
    def __init__(self, file_name):
        with sqlite3.connect(file_name) as self.conn:
            self.curs = self.conn.cursor()

    def create_table(self):
        query = Query.create_table_query
        self.curs.execute(query)
        self.conn.commit()

    def insert_in_table(self, car_mark, car_model, car_year, car_price,url):
        query = Query.insert_query.format(car_mark, car_model, car_year, car_price,url)
        self.curs.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()










