import pytest
from selenium import webdriver

#tujuan dasar : agar addres dan result assert tidak berulang

drv = webdriver.Firefox()
drv.minimize_window()
drv.implicitly_wait(10)

openpages = [
    ("http://google.com", "Goo"),
    ("https://rahulshettyacademy.com/dropdownsPractise","QAClickJ")
    ]
@pytest.mark.parametrize('addr,result_title', openpages) #perhatikan penulisa kutip2nya
def test_openpages(addr,result_title):
    drv.get(addr)
    Title = drv.title
    assert result_title in Title    #bisa juga Title == result_title (biasanya dipake tes login user & pass)

#maka dibawah ini tidak perlu lg dibuat utk buka halaman lain
#krn sdh dijadikan 1 fungsi def diatas

#def test_open_google():
#    drv.get('http://google.com')
#    Title = drv.title
#    assert Title == 'Google'

#def test_open_rahulweb():
#   drv.get('https://rahulshettyacademy.com/dropdownsPractise/')
#    Title2 = drv.title
#    assert 'QAClickJ' in Title2