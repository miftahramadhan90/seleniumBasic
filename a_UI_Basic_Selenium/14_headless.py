'''
Headles utk melakukan test tanpa membuka browser.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True
options.add_experimental_option('excludeSwitches', ['enable-logging'])

drv = webdriver.Chrome(options=options)
drv.get('https://google.com')
print(drv.title)
