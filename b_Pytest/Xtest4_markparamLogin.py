from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pytest
import time

#membuat testcase(negatif) scenario Login pada web demoqa.com
Credentials = [
    ('user1','asdasdkasd'),     #data user salah, pass benar
    ('user2','pass2'),     #data user benar, pass salah
    ('user3','pass3')] #data user salah, pass salah

drv = webdriver.Firefox()
drv.maximize_window()
drv.implicitly_wait(20)

@pytest.mark.parametrize('userid,pwd', Credentials)
def test_logingagal(userid,pwd):
    drv.get('https://demoqa.com/login')
    drv.find_element(By.ID, 'userName').send_keys(userid)
    drv.find_element(By.ID, 'password').send_keys(pwd)
    drv.find_element(By.XPATH, "//button[@id='login']").click()
    #time.sleep(1)
    mess = drv.find_element(By.ID, "name").text
    assert mess == "Invalid username or password!"



