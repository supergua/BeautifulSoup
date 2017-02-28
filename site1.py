from bs4 import BeautifulSoup
import requests

url = 'http://www.tripadvisor.cn/Hotels-g298566-Osaka_Osaka_Prefecture_Kinki-Hotels.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select('div.listing_title > a')
imgs = soup.select('img[width="180"]')
cates = soup.select('div.clickable_tags')
# print(titles, imgs, cates)

for title, img, cate in zip(titles, imgs, cates):
    data = {
        'title': title.get_text(),
        'img': img.get('src'),
        'cate': list(cate.stripped_strings),
    }
    print(data)
