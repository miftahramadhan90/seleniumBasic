from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
drv = webdriver.Chrome(options=options)
drv.implicitly_wait(10)

drv.get('http://the-internet.herokuapp.com/windows')    #cth halaman saat diklik linknya membuka tab browser baru.
drv.find_element(By.XPATH, '//*[@id="content"]/div/a').click()

firstwindow = drv.window_handles[0]
secondwindow = drv.window_handles[1]
time.sleep(2)
drv.switch_to.window(firstwindow)
time.sleep(2)
drv.switch_to.window(secondwindow)

