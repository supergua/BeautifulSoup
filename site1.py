from bs4 import BeautifulSoup
import requests
from multiprocessing import Pool


url = 'http://pop-api.pjbest.com/pop-apis/'
def get_apis(num):
    while True:
        wb_data = requests.get(url)
        num = num + 1
        print(num)

if __name__ == '__main__':
    pool = Pool(processes=2)
    pool.map(get_apis(0))
# for title, img, cate in zip(titles, imgs, cates):
#     data = {
#         'title': title.get_text(),
#         'img': img.get('src'),
#         'cate': list(cate.stripped_strings),
#     }
#     print(data)
