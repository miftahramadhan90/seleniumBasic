from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.by import By  #cth use : drv.find_element(By.CSS_SELECTOR, 'a.masuk').click()

options = webdriver.ChromeOptions()       
options.add_experimental_option('excludeSwitches', ['enable-logging'])
drv = webdriver.Chrome(options=options)

'''Ciri2 path berisi frame end-pathnya biasanya : /iframe, /frameset, or /frame'''
drv.get('https://the-internet.herokuapp.com/iframe') 

drv.implicitly_wait(20)

drv.switch_to.frame('mce_0_ifr')                #MASUK ke iframe ->inspect element bisa berupa : iframe id, frame name, or index
drv.find_element(By.CSS_SELECTOR, "body[id=tinymce] p").clear()
drv.find_element(By.CSS_SELECTOR, "body[id=tinymce] p").send_keys('HALO INI TEXT PERTAMA SAYA DI IFRAME')
print(str(drv.find_element(By.CSS_SELECTOR, "body[id=tinymce] p").text))
drv.switch_to.default_content()      #KELUAR dari iframe ke halaman default page html
print(str(drv.find_element(By.CSS_SELECTOR, 'div[class=example] h3').text))