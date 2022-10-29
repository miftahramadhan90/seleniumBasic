from argparse import Action
from selenium import webdriver               #cth use : drv.find_element_by_id("username").send_keys("idejongkok")
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()       #buat ini
options.add_experimental_option('excludeSwitches', ['enable-logging']) #buat ini

drv = webdriver.Chrome(options=options)
drv.maximize_window()
drv.get("https://demoqa.com/menu")
drv.implicitly_wait(60)

#close popup modal iklan 
# drv.find_element(By.XPATH, "//a[@id='close-fixedban']/img").click()
# time.sleep(2)

'''CARA 1 hover menu'''
#ActionChains(drv).move_to_element(drv.find_element(By.XPATH,"//div[@class='nav-menu-container']/ul/li[2]/a")).perform()

'''CARA 1 hover menu : Extract method actions chain & web element ke dlm object'''

action = ActionChains(drv)
menu1 = drv.find_element(By.XPATH,"//div[@class='nav-menu-container']/ul/li[2]/a")
submenu3 = drv.find_element(By.XPATH, "//a[contains(text(), 'SUB SUB LIST')]")
subsubmenu2 = drv.find_element(By.XPATH, "//a[contains(text(), 'Sub Sub Item 2')]") 
subsubmenu1 = drv.find_element(By.XPATH, "//a[contains(text(), 'Sub Sub Item 1')]")
''' bisa .double_click(), drag_and_drop(), send_keys(), move_to_element(), context_click(), dll'''
action.move_to_element(menu1).perform() # Move to element = Hover(gerakin mouse aja ke elementnya)
action.move_to_element(submenu3).perform() 
action.click(subsubmenu2).perform() #jik mau klik atau doubleclick bs langsung methodenya / tanpa move to element
action.double_click(subsubmenu1).perform()

# Klik Kanan 
action.context_click(subsubmenu2).perform()




