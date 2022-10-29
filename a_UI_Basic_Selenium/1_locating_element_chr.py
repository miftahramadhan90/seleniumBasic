from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.by import By  #cth use : drv.find_element(By.CSS_SELECTOR, 'a.masuk').click()
from selenium.webdriver.common.keys import Keys
import time 

#pilih salah 1 sesuai browser
drv = webdriver.Firefox(executable_path=r'C:\webdriver\geckodriver.exe')
#drv = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe') 
#drv = webdriver.Ie(executable_path=r'C:\webdriver\IEDriverServer.exe')

#SAMPLE WEB utk Latihan
drv.get('https://demoqa.com/alerts')
#('https://demoqa.com/alerts')                          
#('http://the-internet.herokuapp.com/login') 

#LOCATING ELEMENT :
#drv_.find_element_by_id("username").send_keys("idejongkok")                         #by id
#drv.find_element_by_name("password").send_keys("123456")                           #by name
#drv.find_element_by_partial_link_text("Elemental Sele").click()                    #by partial linktext
#drv.find_element_by_class_name("masuk").click()                                    #by class name
#drv.find_element_by_xpath('/html/body/div[1]/div/div/div/div[4]/div/a[2]').click() #by XPATH

#tag_a = drv.find_elements_by_tag_name("a")                                         #by tag a via elementss
#print(len(tag_a))                                                                  #liat jumlah tag a di dlm halaman

#drv.find_element_by_css_selector("a.masuk").click() #by css selector
#drv.find_element(By.CSS_SELECTOR, 'a.masuk').click()

#drv.find_element_by_css_selector("body > div.framebar-desktop > div > div > div > div.dtkframebar__user.pull-right > div > a.masuk.to_login.box_modal_dtkid.dtkframebar__btn.gtm_framebardc_masuk").click() # copy selector dipakai jika css nya tdk ada




