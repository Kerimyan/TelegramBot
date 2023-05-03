import requests
from bs4 import BeautifulSoup


url = 'https://auto.am/offer/2913766'


response = requests.get(url=url)

soup = BeautifulSoup(response.text, 'html.parser')

year = int(soup.find(class_='ad-title').find_all('a')[1].text)
print('year: ',year)

mark = str(soup.find(class_='ad-title').find_all('a')[2].text)
print('mark: ',mark)

model = str(soup.find(class_='ad-title').find_all('a')[3].text)
print('model: ',model)

# price = str(soup.find(class_='ad-title').find(class_='right').find_all('li')[0].text)
price = int(str(soup.find(class_='ad-title').find(class_='fnum').text).replace(' ', ''))
print('price: ',price)







