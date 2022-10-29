from turtle import down
from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.by import By  #cth use : drv.find_element(By.CSS_SELECTOR, 'a.masuk').click()
import pyautogui
import time

options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging'])
drv = webdriver.Chrome(options=options)

drv.get('https://rahulshettyacademy.com/AutomationPractice/')
drv.implicitly_wait(20)
drv.maximize_window()
pyautogui.press("PgDn")
time.sleep(2)
assert drv.find_element(By.ID, 'displayed-text').is_displayed()
time.sleep(1)
drv.find_element(By.ID, 'hide-textbox').click()
assert not drv.find_element(By.ID, 'displayed-text').is_displayed()
time.sleep(1)
drv.close()