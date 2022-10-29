from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = webdriver.FirefoxOptions()
options.headless = True

drv = webdriver.Firefox()               
drv.get('https://demoqa.com/login')
drv.implicitly_wait(15)
drv.get_screenshot_as_file('ss.png')