from imaplib import Time2Internaldate
from selenium import webdriver

drv = webdriver.Firefox()
drv.minimize_window()
drv.implicitly_wait(10)

def test_open_google():
    drv.get('http://google.com')
    Title = drv.title
    assert Title == 'Google'

def test_open_rahulweb():
    drv.get('https://rahulshettyacademy.com/dropdownsPractise/')
    Title2 = drv.title
    assert 'QAClickJ' in Title2

##pengulangan drv.get tidak baik, maka next akan memakai @mark.parametrize()
##selanjutnya pembahasan di file test_markparamDasar & test_scenarioLogin
