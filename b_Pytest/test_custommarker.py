#========================================
'''CUSTOME MARKER PYTEST
Latar belakang  : jika suatu saat diminta test hanya testcase tertentu saja, maka bs gunakan fitur custom marker
Cutome marker   : membuat penanda pada setiap testcase yg dibuat, agar sewaktu2 bisa run testcase itu saja
prerequise      : buat file pytest.ini dlm 1 folder (isinya liat di file pytest.ini)
code            : @pytest.mark.NAMA_MARKERNYA
cara run        : pytest Test_File.py -v -m NAMA_MARKERNYA 
'''
#========================================
from selenium.webdriver.common.by import By
import pytest
import time

#=========================================
#@pytest.mark.usefixtures("setup")
class TestDemoqa:
    
    def test_print(self):
        print('TEST CASE LOGIN SUKSES & LOGIN GAGAL ')
    
    #=======================================================================================================
    '''SCENARIO LOGIN -> TEST CASE ID 2 sd 4 : LOGIN MENGGUNAKAN USER DAN PASS INVALID SEBANYAK 3X'''
    #=======================================================================================================
    
    @pytest.mark.testloginberhasil          # Custome Marker dengan nama : testloginberhasil
    def test_loginberhasil(self, setup, loginvalid):                   #TEST CASE LOGIN SUKSES
        setup.find_element(By.ID, 'userName').send_keys(loginvalid[0])
        time.sleep(2)
        setup.find_element(By.ID, 'password').send_keys(loginvalid[1])
        time.sleep(2)
        '''setup.find_element(By.XPATH, '//*[@id="close-fixedban"]/img').click()
        time.sleep(1)'''
        setup.find_element(By.XPATH, "//button[@id='login']").click()
        time.sleep(2)
        messg = setup.find_element(By.XPATH, "//div[@class='main-header']").text
        assert messg == 'Profile'

    # #=======================================================================================================
        '''SCENARIO LOGIN -> TEST CASE ID 2 sd 4 : LOGIN MENGGUNAKAN USER DAN PASS INVALID SEBANYAK 3X'''
    # #=======================================================================================================
    @pytest.mark.testlogingagal                             # Custome Marker dengan nama : testlogingagal
    def test_logingagal(self, setup, logininvalid):                  #TEST CASE LOGIN GAGAL 3x input
        setup.find_element(By.ID, 'userName').send_keys(logininvalid[0])
        setup.find_element(By.ID, 'password').send_keys(logininvalid[1])
        '''time.sleep(2)
        setup.find_element(By.XPATH, '//*[@id="close-fixedban"]/img').click()
        time.sleep(2)'''
        setup.find_element(By.XPATH, "//button[@id='login']").click()
        time.sleep(1)
        mess = setup.find_element(By.ID, "name").text
        assert mess == "Invalid username or password!"
