'''BASIC'''
from selenium.webdriver.support.ui import Select # buat dropdown use Select()
from selenium import webdriver              
from selenium.webdriver.common.by import By
import time     
import pyautogui                                

options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging']) 

drv = webdriver.Chrome(options=options)
drv.maximize_window()
drv.implicitly_wait(250)
drv.get('https://demoqa.com/select-menu')

#'''OLD STYLE : Biasanya saat inspect ada <select>'''
pilihan = Select(drv.find_element(By.ID, 'oldSelectMenu'))
pilihan.select_by_visible_text('Yellow')    # <option value="3">Yellow</option>
time.sleep(1)
pilihan.select_by_value('4')                # <option value="4">Purple</option>
time.sleep(1)
pilihan.select_by_index(0)                   # balik lg ke index 0 awal -> red : <option value="red">Red</option>
time.sleep(2)

##select one only
a = drv.find_element(By.XPATH, '//*[@id="selectOne"]/div/div[1]/div[1]')
a.click()
pyautogui.write('Prof.')
pyautogui.press('enter')

