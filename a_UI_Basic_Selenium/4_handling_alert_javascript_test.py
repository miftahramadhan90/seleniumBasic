import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging']) 

"""JIKA MAU TEST FILE INI, UBAH DULU NAMA FILENYA KE test_, krn sdh menggunakan def(fungsi) pytest"""
urlsatu = 'https://demoqa.com/alerts'
urldua = 'https://admin:admin@the-internet.herokuapp.com/basic_auth' ## khsus utk alert pop up auth login 

drv = webdriver.Chrome(options=options)
drv.get(urldua)    #cth halaman untuk case popup/alert notif
drv.implicitly_wait(15)
time.sleep(1)
drv.maximize_window()
time.sleep(1)

'''alert hany button OK : dengan menerapkan validasi text java alertnya '''
def test_alert1():
    drv.find_element(By.ID, 'alertButton').click() #<<<---- Button menghasilkan 1 pilihan alert (ok)
    time.sleep(1)
    alert1 = drv.switch_to.alert
    printalert = alert1.text
    alert1.accept()                  # <<<-----fungsi handling alert 1 pilihan : OK(Accept)
    time.sleep(1)
    assert printalert == 'You clicked a button'

def test_alert2():
    '''Alert 2 Pilihan Accept/Dismiss(ok/cancel)'''
    drv.find_element(By.ID, 'confirmButton').click() #<<<---- Button menghasilkan 2 pilihan alert (ok atau cancel)
    time.sleep(1)
    drv.switch_to.alert.dismiss()                   # <<<-----fungsi handling alert 2 pilihan (ok/Cancel) : memilih cancel(Dismiss)
    time.sleep(1)

def test_alertprompt():
    '''Alert Prompt Input Isian'''
    drv.find_element(By.ID, 'promtButton').click() #<<<---- Button menghasilkan isian textbox yg hrs diisi
    time.sleep(1)
    drv.switch_to.alert.send_keys('miftah ramadhan')  # <<<-----fungsi handling alert mengisi textboxt alert 
    time.sleep(2)
    drv.switch_to.alert.accept()
    b = drv.find_element(By.XPATH, "//span[@id='promptResult' and @class='text-success']").text
    assert 'miftah' in b

'''alert pop up auth login isi user dan pass '''
# @pytest.mark.alertuserpass
# def test_alert_login_user_pass():
#     pass
'''
langsung pakai urldua dimasukin -> admin:admin@
'''
# urldua = 'https://admin:admin@the-internet.herokuapp.com/basic_auth'

# drv = webdriver.Chrome(options=options)
# drv.get(urldua)