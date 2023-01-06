from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://www.tiket.com/')
title = driver.title
button_hotel = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[2]/div[1]/section[1]/div/div/div[2]/div[1]/section/div/div/div[2]/button')
button_hotel.click()

# ambilText = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/div[2]/div[1]/section[1]/div/div/div[1]/div/h2')
# print(ambilText.text)

# searchInput = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/header/div/div[3]/div[1]/div/label/div/div/div/label/input')
# searchInput.send_keys('uhuy')

# hotel = driver.find_element(By.XPATH,'//*[@id="__next"]/main/div[1]/header/div/div[3]/div[2]/div/div/ul/li[2]/a')
# hotel.click()
x = (By.XPATH,'//*[@id="__next"]/main/div[1]/div[2]/div[1]/section[1]/div/div/div[2]/div[2]/div[1]/div/div[2]/div')
try:
    WebDriverWait(driver,5).until(EC.presence_of_element_located(x))
    print('nemu bannernya')
except TimeoutException:
    print('kaga muncul bang')
    pass

sleep(5)


