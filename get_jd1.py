from bs4 import BeautifulSoup
import requests
import pymongo


url = 'https://list.jd.com/list.html?cat=9987,653,655&page=2'

client = pymongo.MongoClient('localhost', 27017)
jddata = client['jddata']
sheet_url = jddata['sheet_url']
new_data = []
#jd_urls = ()
wb_data = requests.get(url)
wb_data.encoding = wb_data.apparent_encoding
soup = BeautifulSoup(wb_data.text, 'lxml')
items_ids = soup.select('li.gl-item div.gl-i-wrap.j-sku-item')[0]

print(items_ids.get('data-sku'))
# item_data = {}
# for index, item_id in enumerate(items_ids):
#     url = "http://item.jd.com/" + item_id.get('data-sku') + ".html"
#     # tmp = list(jd_urls)
#     # tmp.append(url)
#     # jd_urls = tuple(tmp)
#     item_data = {
#         'index': index,
#         'item_id': item_id.get('data-sku'),
#         'item_url': url,
#     }
#     sheet_url.insert_one(item_data)


# titles = soup.select('li.gl-item a em')
# prices = soup.select('li.gl-item div.p-price  strong  i')
# items_id = soup.select('li.gl-item')[0].get('data-sku')
#
# for title, price in zip(titles, prices):
#     data = {
#         'title': title.get_text(),
#         'price': price.get_text(),
#     }
#     new_data.append(data)
# new_data = sorted(data, key=lambda k: k['price'])
# list = sorted(new_data, key = lambda k: float(k['price']))
# for i in list:
#     print(i)
