from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver import ActionChains

url = 'http://hotels.ctrip.com/hotel/shanghai2#ctm_ref=hod_hp_sb_lst'

driver = webdriver.Chrome()
driver.get(url)

name_counter = 1
page = 0
time.sleep(3)
try:
    driver.find_element_by_class_name('fl_wrap_close').click()
except ValueError:
    print("No AD need to be closed!")

while page < 10:
    soup = BeautifulSoup(driver.page_source, 'lxml')
    titles = soup.select('h2 > a')
    rates = soup.select('span.hotel_value')
    imgs = soup.select('li.pic_medal > div > a > img')

    for title, rate, img in zip(titles, rates, imgs):
        data = {
            'title': title.get('title'),
            'rate': rate.get_text(),
            'img': img.get('src'),
        }
        print(data)
    time.sleep(3)
    name_counter += 1
    element = driver.find_element_by_id('downHerf')
    ActionChains(driver).move_to_element(element).perform()
    element.click()
    time.sleep(2)
    page += 1

print(name_counter)
driver.quit()
