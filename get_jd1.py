from bs4 import BeautifulSoup
import requests

url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&offset=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&psort=3&click=0'

new_data = []
wb_data = requests.get(url)
wb_data.encoding = wb_data.apparent_encoding
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select('li.gl-item a em')
prices = soup.select('li.gl-item div.p-price  strong  i')
items_id = soup.select('li.gl-item')[0].get('data-sku')

print(items_id)
'''
for title, price in zip(titles, prices):
    data = {
        'title': title.get_text(),
        'price': price.get_text(),
    }
    new_data.append(data)
#new_data = sorted(data, key=lambda k: k['price'])
list = sorted(new_data, key = lambda k: float(k['price']))
for i in list:
    print(i)
'''