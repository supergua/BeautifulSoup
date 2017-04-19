from bs4 import BeautifulSoup
import requests
from time import sleep

remove_items = ['自动','ATM','手自一体','半自动','CVT','双离合','后置','中置','DCT']
# auto = '自动'
# amt = 'AMT'
# atmt = '手自一体'
# half_auto = '半自动'
# cvt = 'CVT'
# dualt = '双离合'
# houzhi = '后置'
# zhongzhi = '中置'
# elec = '电动'
# dct = 'DCT'
item_list = []
new_list = []
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}
item_data = {}

def get_items():
    soup = BeautifulSoup(open("car.html"), 'lxml')
    bands = soup.select('div.ul-name a')
    urls = soup.select('div.ul-name a')
    for band, url in zip(bands, urls):
        item_data = {
            'band': band.get_text(),
            'url': url.get('href'),
        }
        item_list.append(item_data)
    return item_list

def get_info(item_list):
    for band_info in item_list:
        sleep(1)
        flag = False  # 表示纯手动
        url = band_info['url'] + 'price.html'

        wb_data = requests.get(url, headers=headers)
        soup = BeautifulSoup(wb_data.text, 'lxml')
        cars_info = soup.select('div.interval01-list-cars-infor p span')

        for item in remove_items:
            for car in cars_info:
                if item in car.get_text():
                    #print("发现 " + car.get_text() + band_info['band'])
                    flag = True
                    break
        if flag == False:
            new_list.append(band_info)
        else:
            pass

        # for car in cars_info:
        #     if auto in car.get_text():
        #         print("发现自动挡 " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif amt in car.get_text():
        #         print("发现amt " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif half_auto in car.get_text():
        #         print("发现半自动 " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif cvt in car.get_text():
        #         print("发现CVT " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif dualt in car.get_text():
        #         print("发现双离合 " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif houzhi in car.get_text():
        #         print("发现后置车 " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif zhongzhi in car.get_text():
        #         print("发现中置车 " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif atmt in car.get_text():
        #         print("发现手自一体车 " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif elec in car.get_text():
        #         print("发现电动车 " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     elif dct in car.get_text():
        #         print("发现DCT " + car.get_text() + band_info['band'])
        #         flag = True
        #         break
        #     else:
        #         pass
        # if flag == False:
        #     new_list.append(band_info)
        # else:
        #     pass

get_info(get_items())
for i in new_list:
    print(i['band'])
    print(i['url'])