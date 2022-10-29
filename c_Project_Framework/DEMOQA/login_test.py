from utilities.BaseClass import setting
from selenium.webdriver.common.by import By
from pageObjects.loginpageObjects import LoginPage

import pytest
import time

class TestLogin(setting):
    @pytest.mark.testloginberhasil                      # Custome Marker dengan nama : testloginberhasil
    def test_loginberhasil(self, loginvalid):
        loginpage = LoginPage(self.drv)            
        self.drv.find_element(By.ID, 'userName').send_keys(loginvalid['username'])
        self.drv.find_element(By.ID, 'password').send_keys(loginvalid['password'])
        time.sleep(1)
        #close iklan : 
        self.drv.find_element(By.XPATH, '//*[@id="close-fixedban"]/img').click()
        time.sleep(1)
        loginpage.BtnLogin().click()
        #self.drv.find_element(By.XPATH, "//button[@id='login']").click()
        time.sleep(2)
        messg = self.drv.find_element(By.XPATH, "//div[@class='main-header']").text
        assert messg == 'Profile' 
        #time.sleep(1)
        self.drv.find_element(By.ID, "submit").click()      #logout
        self.getLoggers().info(loginvalid)
    # #=======================================================================================================
        '''SCENARIO LOGIN -> TEST CASE ID 2 sd 4 : LOGIN MENGGUNAKAN USER DAN PASS INVALID SEBANYAK 3X'''
    # #=======================================================================================================
    @pytest.mark.testlogingagal                             # Custome Marker dengan nama : testlogingagal
    def test_logingagal(self, login_invalid):                  #TEST CASE LOGIN GAGAL 3x input
        #self.drv.find_element(By.XPATH, '//*[@id="close-fixedban"]/img').click() #close iklan jika dibutuhkan
        self.drv.find_element(By.ID, 'userName').clear() # dipakai jika fixture setup(scope="class")
        time.sleep(1)
        self.drv.find_element(By.ID, 'password').clear()
        time.sleep(1)
        self.drv.find_element(By.ID, 'userName').send_keys(login_invalid['username'])
        self.drv.find_element(By.ID, 'password').send_keys(login_invalid['password'])
        self.drv.find_element(By.XPATH, "//button[@id='login']").click()  
        mess = self.drv.find_element(By.ID, "name").text
        assert mess == "Invalid username or password!"
        self.getLoggers().info(login_invalid)
        
        #self.drv.refresh()
