from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

drv = webdriver.Chrome()

drv.get('https://demoqa.com/droppable')
drv.maximize_window()
drv.implicitly_wait(90)

drag_item = drv.find_element_by_css_selector('#draggable')
drop_place = drv.find_element_by_class_name('drop-box')
act = ActionChains(drv)
time.sleep(2)
act.drag_and_drop(drag_item, drop_place).perform()