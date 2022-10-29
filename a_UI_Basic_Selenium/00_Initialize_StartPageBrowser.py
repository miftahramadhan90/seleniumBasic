from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.by import By  #cth use : drv.find_element(By.CSS_SELECTOR, 'a.masuk').click()
from selenium.webdriver.common.keys import Keys
import time 

#CARA INITIALIZE Start Page 3 DRIVER BROWSER YG SERING DIPAKAI | path sesuaikan ditempat driver .exe nya
#pilih salah 1 sesuai browser 
drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
drv = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') 
drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')
drv = webdriver.Chrome()

# hilangin bluetooth driver Chrome :


