from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# contoh button yg menggunakan dynamic xpath
drv = webdriver.Firefox()
drv.get('https://demoqa.com/buttons')
drv.implicitly_wait(20)
drv.find_element(By.XPATH, "//form[@id='userForm']/div[3]/div[2]/div/label[text()='Male']").click()


'''
rumus create dynamic xpath sendiri :
//TagName[starts-with(@attributeName
//*[contains(@name,'Click Me')]
//button[contains(@name,'Click Me')] -> contains/starts-with/ends-with
//button[contains(text(),'Click Me') and starts-with(text(),'Click Me')]
//button[starts-with(text(),'Click Me')]

//button[text()='Click Me']

'''