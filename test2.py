#coding:utf-8
from selenium import webdriver
b = webdriver.Chrome(r"D:\pythonproj\bs\chromedriver.exe")
b.get("http://www.baidu.com")
b.find_element_by_id("kw").send_keys(u"hello world")
b.find_element_by_id("su").click()