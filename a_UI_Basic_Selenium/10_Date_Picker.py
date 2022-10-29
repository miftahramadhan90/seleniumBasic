from selenium import webdriver
import pyautogui
import time

brw = webdriver.Chrome()

brw.get('https://jqueryui.com/datepicker/')
brw.implicitly_wait(30)
time.sleep(3)

brw.switch_to.frame(brw.find_element_by_class_name('demo-frame'))
brw.find_element_by_id('datepicker').click()
time.sleep(2)
brw.find_element_by_css_selector('.ui-datepicker-calendar > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > a:nth-child(1)').click() 
time.sleep(2)
brw.find_element_by_id('datepicker').clear()
time.sleep(2)
brw.find_element_by_id('datepicker').send_keys('10/01/2021')
time.sleep(2)
pyautogui.press('enter')