from bs4 import BeautifulSoup
import time
from selenium import webdriver

url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C% \
        BA&psort=3&cid2=653&cid3=655&stock=1'

driver = webdriver.Chrome()
driver.get(url)
new_data = []
name_counter = 1
page = 0
time.sleep(2)
try:
    driver.find_element_by_class_name('btn-sure').click()
except:
    print("No AD need to be closed!")

while page < 10:
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    titles = soup.select('li.gl-item a em')
    prices = soup.select('li.gl-item div.p-price  strong  i')
    items_id = soup.select('li.gl-item')

    for title, price, item_id in zip(titles, prices, items_id):
        data = {
            'title': title.get_text(),
            'price': price.get_text(),
            'item_id': item_id.get('data-sku'),
        }
        new_data.append(data)
    name_counter += 1
    driver.find_element_by_class_name('pn-next').click()
    page += 1

newlist = sorted(new_data, key = lambda k: float(k['price']))
for i in newlist:
    print(i)

driver.quit()




