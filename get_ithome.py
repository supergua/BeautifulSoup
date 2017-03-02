from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Cookie': 'BEC=5BEB2575CAC8C8F2ECE5DAEF6A861002|WLY6d|WLY6d; Hm_lvt_cfebe79b2c367c4b89b285f412bf9867=1487828438,1487913689,1488155657,1488337525; Hm_lpvt_cfebe79b2c367c4b89b285f412bf9867=1488337525',
}

url = 'http://www.ithome.com'
wb_data = requests.get(url,headers=headers)
wb_data.encoding = wb_data.apparent_encoding
soup = BeautifulSoup(wb_data.text, 'lxml')
titles = soup.select('span.title > a')
urls = soup.select('span.title > a')

for title, url in zip(titles, urls):
    data = {
        'titie': title.get_text(),
        'url': url.get('href'),
    }
    print(data)
