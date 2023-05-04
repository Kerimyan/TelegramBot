class Query:
    create_table_query = "CREATE TABLE IF NOT EXISTS cars " \
                         "(id INTEGER PRIMARY KEY," \
                         "car_mark varchar(30)," \
                         "car_model varchar(30)," \
                         "car_year varchar(30), " \
                         "car_price varchar(30), " \
                         "url varchar(30));"
    insert_query = "INSERT INTO cars (car_mark, car_model, car_year, car_price,url) values ('{}', '{}', '{}', '{}','{}');"


