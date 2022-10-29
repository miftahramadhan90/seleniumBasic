from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, drv):
        self.drv = drv
    
    buttonlogin = (By.XPATH, "//button[@id='login']")
    
    def BtnLogin(self):
        return self.drv.find_element(*LoginPage.buttonlogin)
    
