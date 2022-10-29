'''BASIC'''
from unittest import TestCase
from selenium import webdriver              
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys #buat action keyboar enter, esc
from selenium.webdriver.common.action_chains import ActionChains #perform mouse: menu hover, dragNdrop, dll
from selenium.webdriver.support.ui import Select # buat dropdown use Select()
drv = webdriver.Chrome()

'''lib utk try: except :, bisa dipakai jg utk wait'''
from selenium.webdriver.support import expected_conditions as EC #utk handling explicity wait / try except 
from selenium.webdriver.support.ui import WebDriverWait # (ide jongkok, agak sulit ngebaca codenya krn panjang, dn pakai try except)
from selenium.common.exceptions import TimeoutException #dipakai utk except TimeoutException : --> pasangannya dengan try:

'''Lib utk wait'''
from selenium.webdriver.support.wait import WebDriverWait # rahulshetty tanpa try excep bisa pakai ini (lbh mudah bacanya)
wait = WebDriverWait(drv,10) #buat dipanggil nanti saat pakai explicit wait di baris manapun

'''LAIN LAIN'''
import pyautogui                        #utk press, write, liat contoh di materi Upload Files | datepicker
import time                                     
'''OPTIONS CHROME : Bluetooth driver message'''
options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging']) 

'''OPTIONS HEADLESS - PYTEST RUN tanpa open browser'''
options = webdriver.ChromeOptions()  # utk mozilla : FirefoxOptions()
options.headless = True

'''bisa utk hadle alert pop up notification/javascript --> sdh dicoba telegram berhasil'''
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)  


'''Open the new window'''
drv.execute_script("window.open()")
