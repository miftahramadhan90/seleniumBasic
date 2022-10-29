from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging']) 

url = 'https://usernya:passwordnya@the-internet.herokuapp.com/basic_auth' ## 

drv = webdriver.Firefox()
drv.get(url)    
drv.implicitly_wait(15)
time.sleep(1)
drv.maximize_window()
time.sleep(1)