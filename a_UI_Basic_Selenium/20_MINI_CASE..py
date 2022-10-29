from cgitb import text
from msilib.schema import Error
import time
from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.by import By  #cth use : drv.find_element(By.CSS_SELECTOR, 'a.masuk').click()
from selenium.webdriver.support import expected_conditions as EC #utk handling explicity wait / try except 
#from selenium.webdriver.support.ui import WebDriverWait # (ide jongkok, agak sulit ngebaca codenya krn panjang)
from selenium.webdriver.support.wait import WebDriverWait #atau bisa jg ini (ref:rahulshetty)
from selenium.common.exceptions import TimeoutException #utk handling exceptionnya jika gagal

options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging'])
drv = webdriver.Chrome(options=options)
wait = WebDriverWait(drv,10) #buat dipanggil nanti saat pakai explicit wait di baris manapun

drv.get('https://rahulshettyacademy.com/seleniumPractise')

drv.find_element(By.CSS_SELECTOR, 'input.search-keyword').send_keys('ber')
time.sleep(2)   #!!!!!

'''CASE 1 : iter webelemen label utk mengextraxt text lalu di append ke dlm list'''
#//div[@class='product-action']/button/parent::div/parent::div/h4 --> format xpath inspect balikan ke parent agar bs dipakai bersama labelnya utk looping juga

addchartbuttons = drv.find_elements(By.XPATH, "//div[@class='product-action']/button")
list1 = []          #List kosong utk tempat simpan iterasi label add to chart
list2 = []          #List kosong utk tempat simpan iterasi di halaman konfirmasi chart / .promoCode

for button in addchartbuttons:
    #print(button.find_element(By.XPATH, "parent::div/parent::div/h4").text)
    list1.append(button.find_element(By.XPATH, "parent::div/parent::div/h4").text) #penggunaan xpath balikan parent ambil labelnya
    button.click()
#print(list1)

drv.find_element(By.XPATH, "//img[@alt='Cart']").click()
drv.find_element(By.XPATH, "//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']").click()
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoCode")))

confirm_chart = drv.find_elements(By.CSS_SELECTOR, ".product-name")
for konfirm in confirm_chart:
    list2.append(konfirm.text)
#print(list2)

jumlah_sblm_disc = drv.find_element(By.CSS_SELECTOR, '.discountAmt').text
drv.find_element(By.CSS_SELECTOR, '.promoCode').send_keys('rahulshettyacademy')
drv.find_element(By.CSS_SELECTOR,".promoBtn").click()
promoinfo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.promoInfo'))).text
jumlah_stlh_disc = drv.find_element(By.CSS_SELECTOR, '.discountAmt').text

assert int(jumlah_sblm_disc) > float(jumlah_stlh_disc)
assert list1 == list2, 'list 1 dan list 2 tidak sama'
assert promoinfo == 'Code applied ..!', 'text promo info salah / tidak atau belum keluar'

#print(promoinfo)

'''#Buat Validasi jumlah :'''
total = drv.find_elements(By.XPATH, '//tr/td[5]/p') ##ekstraks 3 elementss : 48, 160. 180

sums = int()
for tot in total:
    sums += int(tot.text)
print(type(sums))

TotAmount = drv.find_element(By.CSS_SELECTOR, '.totAmT')

assert int(TotAmount.text) == sums, 'Jumlah total tidak sama dgn TotAmount'





drv.close()
    



'''ide jongkok :'''
# drv.get('https://demoqa.com/alerts')

# drv.find_element_by_id("timerAlertButton").click() #kondisi akan muncul alert 5 dtk setelah diclick button
# try:
#     WebDriverWait(drv, 10).until(EC.alert_is_present()) #akan menunggu 10 dtk sampai kondisi alert is present
#     drv.switch_to.alert.accept() # setelah muncul alert akan di accept/ok
#     print("Alert sudah di pencet ok") #utk log code : kondisi alert sdh diklik
# except TimeoutException: #manggil dr lib timeoutexception
#     print ("alert tidak sempat muncul / tidak dipencet") # bs ditest webdriverwaitnya ganti jadi 3 detik
#     pass # jika waktu yg sdh ditentukan alert tidak sempat muncul krn timeout, maka dipass ke code selanjutnya




