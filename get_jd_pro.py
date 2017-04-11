from bs4 import BeautifulSoup
import time
import pymongo
from selenium import webdriver

#数据库连接
client = pymongo.MongoClient('localhost', 27017)
jddata = client['jddata']
sheet_url = jddata['sheet_url']

url = 'https://list.jd.com/list.html?cat=9987,653,655'
driver = webdriver.Chrome()
driver.get(url)
new_data = []
name_counter = 1
page = 0
item_data = {}
time.sleep(2)
try:
    driver.find_element_by_class_name('btn-sure').click()
except:
    print("No AD need to be closed!")

while page < 10:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    titles = soup.select('li.gl-item a em')
    prices = soup.select('li.gl-item div.p-price  strong  i')
    item_ids = soup.select('li.gl-item div.gl-i-wrap j-sku-item')

    for price, item_id in zip(prices, item_ids):
        item_data = {
            'price': price.get_text(),
            'item_id': item_id.get('data-sku'),
            'item_url': "http://item.jd.com/" + str(item_id.get('data-sku')) + ".html",
        }
        sheet_url.insert_one(item_data)
    name_counter += 1
    driver.find_element_by_class_name('pn-next').click()
    time.sleep(5)
    page += 1


driver.quit()