#========================================
'''PYTEST.FIXTURE pada web demoqa.com'''
#========================================

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time



@pytest.fixture                    # untuk menyatukan set inisialisasi awal browser 
def setup():
    options = webdriver.ChromeOptions() #webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-notifications")
    options.add_experimental_option("detach", True)
    # #options.headless = True
    drv = webdriver.Chrome(options=options)   #               #sdh ditest juga menggunakan chrome berhasil
    drv.maximize_window()               #hati2 min dan max. kadang saat pakai drv firefox/google sering eror, ada efek jg iklan yg tdk bisa diblock
    drv.get('https://demoqa.com/login')
    drv.implicitly_wait(15)
    yield drv                           #mengembalikan nilai satu persatu. // #klo return langsung mengembalikan semua nilai lalu selesai
    #drv.quit()

   
#=======================================================================================================
'''SCENARIO LOGIN -> TEST CASE ID 1 : LOGIN MENGGUNAKAN USER DAN PASS YANG VALID '''
#=======================================================================================================
userpass_succes = [
    ('idejongkok', 'asDF12#$')]         # user benar, pass benar
    
#@pytest.mark.xfail                                          #Arti unexpected pass : contoh testcase dites harusnya gagal dgn pengujian nilai yg kita masukkan, namun malah berhasil(berarti bugs) 
@pytest.mark.parametrize('usrid,pwdd', userpass_succes)
def test_loginberhasil(setup,usrid,pwdd):                   #TEST CASE LOGIN SUKSES
    setup.find_element(By.ID, 'userName').send_keys(usrid)
    setup.find_element(By.ID, 'password').send_keys(pwdd)
    setup.find_element(By.XPATH, '//*[@id="close-fixedban"]/img').click()
    setup.find_element(By.XPATH, "//button[@id='login']").click()
    time.sleep(3)
    messg = setup.find_element(By.XPATH, "//div[@class='main-header']").text
    assert messg == 'Profile'

#=======================================================================================================
'''SCENARIO LOGIN -> TEST CASE ID 2 sd 4 : LOGIN MENGGUNAKAN USER DAN PASS INVALID SEBANYAK 3X'''
#=======================================================================================================
userpass_failed = [
    ('idejongkok','asdasdkasd'),        # user benar, pass salah
    ('asasd','asDF12#$'),               # user salah, pass benar
    ('asde','xcdf')]                    # user salah, pass salah

@pytest.mark.skip                                           #Arti mark skip utk menandai testcase tidak ditest  
@pytest.mark.parametrize('userid,pwd', userpass_failed)
def test_logingagal(setup,userid,pwd):                  #TEST CASE LOGIN GAGAL 3x input
    setup.find_element(By.ID, 'userName').send_keys(userid)
    setup.find_element(By.ID, 'password').send_keys(pwd)
    setup.find_element(By.XPATH, "//button[@id='login']").click()
    #time.sleep(1)
    mess = setup.find_element(By.ID, "name").text
    assert mess == "Invalid username or password!"
