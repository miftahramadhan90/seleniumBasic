from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.by import By  #cth use : drv.find_element(By.CSS_SELECTOR, 'a.masuk').click()
from selenium.webdriver.common.keys import Keys
import time 

#CARA INITIALIZE Start Page 3 DRIVER BROWSER YG SERING DIPAKAI | path sesuaikan ditempat driver .exe nya
#pilih salah 1 sesuai browser
drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
#drv = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') 
#drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')
drv.implicitly_wait(10)         #fungsi implicitly_wait -> utk kondisi internet lemot saat testing web. (10 : detik)
drv.get('https://demoqa.com/login') ##< ditunggu 10 detik proses membuka page ini .
drv.get('https://demoqa.com/books') ##< ditunggu 10 detik proses membuka page ini
drv.find_element_by_id('login').click() ##< ditunggu 10 detik proses menemukan buton ini

#NOTES: 
# untuk alerts pop up tidak bisa dihandle dengan implicitly_wait
# Sekali declare implicitly wait akan menunggu x detik pada setiap proses baris code.
