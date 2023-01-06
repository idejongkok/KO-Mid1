from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# option = webdriver.ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-logging'])

# Tiket.com
driver = webdriver.Chrome()
driver.maximize_window()
# Set Url 
# driver.get("https://www.tiket.com/")
# title1 = driver.title
# print(title1)
# time.sleep(2)

# Web Ke-2 
# driver.maximize_window()
# driver.get("https://www.orangsiber.com/")
# title2 = driver.title
# print(title2)
# time.sleep(2)

# Web Ke-3
# driver.get("https://demoqa.com/")
# title3 = driver.title
# print(title3)
# time.sleep(2)

# # # Web Ke-4 
# driver.get("https://automatetheboringstuff.com/")
# title4 = driver.title
# print(title4)
# time.sleep(2)

# # Web Ke-5 
# driver.get("https://www.tokopedia.com/")
# title5 = driver.title
# print(title5)
# time.sleep(2)

listlink = ['https://www.orangsiber.com/', 'https://www.tiket.com/', 'https://demoqa.com/', 'https://automatetheboringstuff.com/', 'https://www.tokopedia.com/']
name = ['orangsiber.com', 'tiket.com', 'demoqa.com', 'automatetheboringstuff.com', 'tokopedia.com']

# bermain index
i = 0
while i <= len(listlink):
  # print(listlink[i])
  driver.get(listlink)
  print(name[i]+" - "+driver.title)
  i += 1