from bs4 import BeautifulSoup
import requests

url = 'http://hotels.ctrip.com/hotel/chongqing4#ctm_ref=hod_hp_sb_lst'

wb_data = requests.get(url)

soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select('h2 > a')
rates = soup.select('span.hotel_value')
imgs = soup.select('li.pic_medal > div > a > img')
clicks = soup.select('div.c_page > a')

for click in clicks:
    print(click.get_text())
'''
for title, rate, img in zip(titles, rates, imgs):
    data = {
        'title':title.get('title'),
        'rate':rate.get_text(),
        'img':img.get('src'),
    }
    print(data)
'''