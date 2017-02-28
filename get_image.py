from bs4 import BeautifulSoup
import requests
import time

url = 'http://www.tripadvisor.cn/Hotels-g293920-Phuket-Hotels.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
}

mb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(mb_data.text, 'lxml')
