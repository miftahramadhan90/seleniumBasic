from ast import Or
from selenium import webdriver
from selenium.webdriver.common.by import By
import time     

options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
drv = webdriver.Chrome(options=options)
drv.get('https://rahulshettyacademy.com/AutomationPractice/')
drv.implicitly_wait(30)

radiobutton = drv.find_elements(By.XPATH, "//input[@type='radio']") #elements->Jamak : extraxt ke dlm object
radiobutton[2].click()   #masukin index urutannya
assert radiobutton[2].is_selected  #validasi ud terpilih idx 3 atau blm
drv.close()