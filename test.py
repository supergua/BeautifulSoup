from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://www.ithome.com/")
bsObj = BeautifulSoup(html,'lxml')
print(bsObj)
