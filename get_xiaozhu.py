from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.xiaozhu.com/fangzi/3584187630.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')

titles = soup.select('div.pho_info > h4 > em')
addrs = soup.select('div.con_l > div.pho_info > p > span')
prices = soup.select('div.day_l > span')
imgs = soup.select('#curBigImage')
names = soup.select('a.lorder_name')


for title, addr, price, img, name in zip(titles, addrs, prices, imgs, names):
    data = {
        'title':title.get_text('title'),
        'addr':addr.text.rstrip(),
        'price': price.text.rstrip(),
        'img': img.get('src'),
        'name': name.get_text('title'),
    }
    print(data)