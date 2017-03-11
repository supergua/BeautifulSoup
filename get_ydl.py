from bs4 import BeautifulSoup
import requests, time, sqlite3

url = 'http://115.28.51.175/zl.php?key=nbhqdf488'
cx = sqlite3.connect('ydl.db')
cu = cx.cursor()

while 17 - int(time.strftime('%H', time.localtime(time.time()))):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    o2msg = soup.select('span.text-center.data')
    tm = time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    #cx.execute("insert into o2table(time,cl2) values(?,?)", (tm, o2msg[0].get_text()))
    #cx.commit()
    '''获取最近3条记录'''
    last3 = cx.execute("select time,cl2 from o2table order by id DESC limit 3").fetchall()
    for i in last3:
        print("北仑氧动力游泳池实时含氯量："+ i[1] + " 记录时间: " + i[0])
    time.sleep(10)
cx.close()




