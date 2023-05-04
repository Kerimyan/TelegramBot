from bs4 import BeautifulSoup


class CarFinder:
    def __init__(self, response):
        self._response = response
        self._bs = BeautifulSoup(self._response.text, 'html.parser')

    def get_mark(self):
        mark_bs = self._bs.find(class_='ad-title').find_all('a')[2]
        mark = str(mark_bs.text) if mark_bs else None
        return mark

    def get_model(self):
        model_bs = self._bs.find(class_='ad-title').find_all('a')[3]
        model = str(model_bs.text) if model_bs else None
        return model

    def get_year(self):
        year_bs = self._bs.find(class_='ad-title').find_all('a')[1]
        year = int(year_bs.text) if year_bs else None
        return year

    def get_price(self):
        price_bs = self._bs.find(class_='ad-title').find(class_='fnum')
        prise = int(str(price_bs.text).replace(' ', '')) if price_bs else None
        return prise
