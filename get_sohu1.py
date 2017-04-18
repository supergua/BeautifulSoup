from bs4 import BeautifulSoup
import requests
from time import sleep

my_band1 = []
my_band2 = []
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

def get_sohu_car1(pages):
    url = 'https://db.auto.sohu.com/searchcar-0-1-0-0-0-15-0-0-0-1-0-{}-0-0-0-0.shtml#resultL'.format(str(pages))
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    bands = soup.select('div.cont li p a.blue')

    for band in bands:
        my_band1.append(band.get_text())
    sleep(2)


def get_sohu_car2(pages):
    url = 'https://db.auto.sohu.com/searchcar-0-1-0-0-0-15-2-0-0-1-0-{}-0-0-0-0.shtml#resultL'.format(str(pages))
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    bands = soup.select('div.cont li p a.blue')

    for band in bands:
        my_band2.append(band.get_text())
    sleep(2)


for i in range(0,5):
    get_sohu_car1(i)

for i in range(0,4):
    get_sohu_car2(i)

print(len(my_band1))
print(len(my_band2))

car1 = set(my_band1)
car2 = set(my_band2)
cars = car1.difference(car2)

for car in cars:
    print(car)
print(len(car))