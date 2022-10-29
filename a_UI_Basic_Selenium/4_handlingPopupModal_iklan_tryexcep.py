#handling pop up iklan :
# //div[@class='btn-modal-close']//i[@class='fa fa-close']
from ast import Try
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()      
options.add_experimental_option('excludeSwitches', ['enable-logging']) 
drv = webdriver.Chrome(options=options)

drv.get('https://tees.co.id')
drv.implicitly_wait(10)

try:
    WebDriverWait(drv,10).until(EC.visibility_of_element_located((By.XPATH, '//body/div[1]')))
    print("pop up muncul")
    drv.find_element(By.XPATH, "//div[@class='btn-modal-close']//i").click()
    print("pop up diclose")

except TimeoutException:
    print('pop up tidak muncul setlah 10 detik ditungguin')
    pass
drv.close()
