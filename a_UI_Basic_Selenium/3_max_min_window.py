from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

#pilih salah 1 sesuai browser:
drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
#drv = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') 
#drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')


drv.get('http://the-internet.herokuapp.com/windows')    #cth halaman saat diklik linknya membuka tab browser baru.
time.sleep(2)
drv.maximize_window()  #<<----Fungsi max win
time.sleep(1)
drv.minimize_window() #<<----Fungsi min win
time.sleep(2)
drv.maximize_window()
time.sleep(2)
drv.refresh()


