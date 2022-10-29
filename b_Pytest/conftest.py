from selenium import webdriver
import pytest

@pytest.fixture()                     
def setup():
    options = webdriver.FirefoxOptions() #webdriver.ChromeOptions()
    #options.add_experimental_option('excludeSwitches', ['enable-logging'])
    #options.headless = True
    drv = webdriver.Firefox(options=options)          
    drv.maximize_window()               
    drv.get('https://demoqa.com/login')
    drv.implicitly_wait(15)
    yield drv
    #drv.get_screenshot_as_file('customarker.png')
    #drv.quit()

#userpass berhasil
@pytest.fixture(params=[('idejongkok', 'asDF12#$')])
def loginvalid(request):
    yield request.param


#userpass salah
@pytest.fixture(params=[('idejongkok', 'asaa'),  # user benar, pass salah - 4 
                        ('asaa', 'asDF12#$'),          # user salah, pass benar - 8
                        ('asaaa', 'asaaaa')])              # user salah, pass salah - 6
def logininvalid(request):
    yield request.param