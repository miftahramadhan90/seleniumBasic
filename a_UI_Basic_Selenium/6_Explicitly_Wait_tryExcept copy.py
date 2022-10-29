from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.by import By  #cth use : drv.find_element(By.CSS_SELECTOR, 'a.masuk').click()
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC #utk handling try conditions 
from selenium.webdriver.support.ui import WebDriverWait #utk menunggu proses tertentu pada halaman muncul/terbuka
from selenium.webdriver.support.wait import WebDriverWait #atau bisa jg ini (ref:rahulshetty)
from selenium.common.exceptions import TimeoutException #utk handling exceptionnya jika gagal

#CARA INITIALIZE Start Page 3 DRIVER BROWSER YG SERING DIPAKAI | path sesuaikan ditempat driver .exe nya
#pilih salah 1 sesuai browser
drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
#drv = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') 
#drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')

drv.get('https://demoqa.com/alerts')

drv.find_element_by_id("timerAlertButton").click() #kondisi akan muncul alert 5 dtk setelah diclick button
try:
    WebDriverWait(drv, 10).until(EC.alert_is_present()) #akan menunggu 10 dtk sampai kondisi alert is present
    drv.switch_to.alert.accept() # setelah muncul alert akan di accept/ok
    print("Alert sudah di pencet ok") #utk log code : kondisi alert sdh diklik
except TimeoutException: #manggil dr lib timeoutexception
    print ("alert tidak sempat muncul / tidak dipencet") # bs ditest webdriverwaitnya ganti jadi 3 detik
    pass # jika waktu yg sdh ditentukan alert tidak sempat muncul krn timeout, maka dipass ke code selanjutnya




