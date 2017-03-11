from bs4 import BeautifulSoup
import time
import pymongo
import requests

#数据库连接
client = pymongo.MongoClient('localhost', 27017)
jddata = client['jddata']
sheet_url = jddata['sheet_url']

# headers
headers = {
    'Cookie': 'user-key=5ab75cde-2cef-46bf-8635-d98017ebf9a8; mt_xid=V2_52007VwMXW1hYUl8eTx1VBWYDFFNcXlFYH0EQbFdhUEBWCVlTRh9OEF8ZYgFBUEFQW1weVR0LBG4CQVpcWwZaGXkaXQVhHxNQQVlRSx5AElgEbAcaYl9oUmofSBBcBmUHFFttW1pa; unpl=V2_ZzNtbUIDFxR0CUJSKR9UVmJUElURUREVcFpGBH0QCQxiVxNaclRCFXMUR1ZnGF4UZwQZX0ZcRxxFCEdkeylbBmYHEF5yVkJVdlxCB31ODFVvABtbS1JFFHI4RVRLGV01ZwYbWEJXRhRzDE9UehlaBGYFEV9CX0olRQ92ZK6S0tzjhcbj4mdEEHINQ1V6GmwEVwIiFixWDhVwAUNUexxdA2MKElxCUUIUcwtEVHMQbARXAA%3d%3d; __jdv=122270672|p.yiqifa.com|t_1_620532|tuiguang|1ee00057c79b4f19b7c14c1a78d84e06|1488530167898; areaId=15; dmpjs=dmp-d151603d10489cb48fda92741f671a8ee1ec195; cn=0; _jrda=1; TrackID=1LzlLs1Z8weM7gEYpiyxN0kWXj5jez0fyClntRuutrqWImWHa_AzBy_3_dzhujnvg4jOR_sP-lxej2E1FFwz4Of0Jv3ciIXhZu_esmSj244w; pinId=XQT1-ByNlNm1ffsfn98I-w; pin=blhkblhk; unick=blhkblhk; _tp=5Ee4PxwQq1d4XUllgEjRRw%3D%3D; _pst=blhkblhk; 3AB9D23F7A4B3C9B=AJJITBQIEBRK6TOQ7XT23VSGS5QI53QJDZIVMNRNXLFLQ65Y5CAY7KN67T4QXKQIFQAX6MAGCGAKO4PCHTDXRWD5KU; ipLoc-djd=15-1158-46341-51590.137967066; ipLocation=%u6D59%u6C5F; listck=4f3b99da221149795e048c03fa64477a; __jda=122270672.14841140758101700723198.1484114076.1488947120.1489107174.101; __jdb=122270672.10.14841140758101700723198|101.1489107174; __jdc=122270672; __jdu=14841140758101700723198',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}


def get_jd_cell_urls(pages):
    url = 'https://list.jd.com/list.html?cat=9987,653,655&page={}'.format(str(pages))
    wb_data = requests.get(url,headers=headers)
    time.sleep(3)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('li.gl-item div.gl-i-wrap.j-sku-item'):
        item_link = "http://item.jd.com/" + link.get('data-sku') + ".html"
        sheet_url.insert_one({'item_id':link.get('data-sku'), 'url': item_link})
        print(item_link)


for i in range(1, 104):
    print(i)
    get_jd_cell_urls(i)

# url = 'https://list.jd.com/list.html?cat=9987,653,655'
# new_data = []
# name_counter = 1
# page = 0
# item_data = {}
# time.sleep(2)
#
# while page < 10:
#     soup = BeautifulSoup(wb_data.text, 'lxml')
#     titles = soup.select('li.gl-item a em')
#     prices = soup.select('li.gl-item div.p-price  strong  i')
#     item_ids = soup.select('li.gl-item div.gl-i-wrap.j-sku-item')
#
#     for price, item_id in zip(prices, item_ids):
#         item_data = {
#             'price': price.get_text(),
#             'item_id': item_id.get('data-sku'),
#             'item_url': "http://item.jd.com/" + str(item_id.get('data-sku')) + ".html",
#         }
#         sheet_url.insert_one(item_data)
#     name_counter += 1
#     driver.find_element_by_class_name('pn-next').click()
#     time.sleep(5)
#     page += 1
#
#
# driver.quit()