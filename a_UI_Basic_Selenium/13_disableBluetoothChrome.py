from selenium import webdriver

options = webdriver.ChromeOptions()       #buat ini
options.add_experimental_option('excludeSwitches', ['enable-logging']) #buat ini

drv = webdriver.Chrome(options=options) #buat ini
drv.get("https://demoqa.com/login")
drv.close()

'''
#klo masih ada eror ini :
ERROR:gpu_init.cc(454)] Passthrough is not supported, GL is disabled, ANGLE is

#coba baca2 ini :
https://exerror.com/errorgpu_init-cc426-passthrough-is-not-supported-gl-is-disabled/
'''