from selenium import webdriver
from time import sleep
from selenium.webdriver.common import by

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://demoqa.com/browser-windows')
driver.find_element(by=By.ID)