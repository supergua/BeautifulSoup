import requests
import re
from bs4 import BeautifulSoup

url = 'http://www.zmz2017.com'

req = requests.get(url)
wb_data = BeautifulSoup(req.text,'lxml')

images = wb_data.find_all(src=re.compile("^http\:\/\/tu.*[a-z]{5}(\.jpg|\.png)$"))
date = wb_data.find_all(src=re.compile("2012"))

print(images)