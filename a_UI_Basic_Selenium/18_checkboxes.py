from ast import Or
from selenium import webdriver
from selenium.webdriver.common.by import By
import time     

options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
drv = webdriver.Chrome(options=options)
drv.get('https://rahulshettyacademy.com/AutomationPractice/')
drv.implicitly_wait(30)

#scenario ceklist semua : step : ambil xpath seluruh cekbox yg attributnya sama, 
                                # lalu extract ke dlm object -> iter objectnya -> setiap berulang clik
cekbox = drv.find_elements(By.XPATH, "//input[contains(@value, 'option')]") #hati2 saat loop: elements(jamak) bs diiter, bkn element(object tunggal)
for i in cekbox:
     i.click()
assert i.is_selected()

#Scene ceklis salah satu aja, ambil xpathnya spesificnya
a = drv.find_element(By.XPATH, "//input[contains(@value, 'option') and @name='checkBoxOption3']")
a.click()
assert a.is_selected()

#scenario ceklist spesifik lebih dari 1 (tidak semua) [hanya pilih opt2 dan opt3]
cekbox = drv.find_elements(By.XPATH, "//input[contains(@value, 'option')]") #hati2 saat loop: elements(jamak) bs diiter, bkn element(object tunggal)

temp = []
for i in cekbox:
     if i.get_attribute('value') == 'option2' or i.get_attribute('value') == 'option3':
          i.click()
          temp.append(i)
assert len(temp) == 2              # atau bs juga assert len(temp) < 10 --> True
