from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
# Set Url 
driver.get("https://demoqa.com/webtables")

i = 1
while i <= 3:
    # Set Klik hapus
    driver.find_element(By.ID,f'delete-record-{i}').click()
    time.sleep(1)
    i+=1

dict = {"1":['nama depannya siapa',]}

# add data 
driver.find_element(By.ID, 'addNewRecordButton').click()
time.sleep(1)

# Mengisi Data 1
driver.find_element(By.ID, 'firstName').send_keys('Jordy Dwi')
time.sleep(1)
driver.find_element(By.ID, 'lastName').send_keys('Prakoso')
time.sleep(1)
driver.find_element(By.ID, 'userEmail').send_keys('jordydwiprakoso@gmail.com')
time.sleep(1)
driver.find_element(By.ID, 'age').send_keys('23')
time.sleep(1)
driver.find_element(By.ID, 'salary').send_keys('3000000')
time.sleep(1)
driver.find_element(By.ID, 'department').send_keys('IT')
time.sleep(1)
# Submit Data
driver.find_element(By.ID, 'submit').click()
time.sleep(1)

# Mengisi Data 2
# add data 
driver.find_element(By.ID, 'addNewRecordButton').click()
time.sleep(1)

driver.find_element(By.ID, 'firstName').send_keys('Alih')
time.sleep(1)
driver.find_element(By.ID, 'lastName').send_keys('Powerty')
time.sleep(1)
driver.find_element(By.ID, 'userEmail').send_keys('aliqwerty@gmail.com')
time.sleep(1)
driver.find_element(By.ID, 'age').send_keys('21')
time.sleep(1)
driver.find_element(By.ID, 'salary').send_keys('2000000')
time.sleep(1)
driver.find_element(By.ID, 'department').send_keys('HRD')
time.sleep(1)
# Submit Data
driver.find_element(By.ID, 'submit').click()
time.sleep(1)

# Mengisi Data 3
# add data 
driver.find_element(By.ID, 'addNewRecordButton').click()
time.sleep(1)

driver.find_element(By.ID, 'firstName').send_keys('Ryan')
time.sleep(1)
driver.find_element(By.ID, 'lastName').send_keys('Santoso')
time.sleep(1)
driver.find_element(By.ID, 'userEmail').send_keys('ryansantoso@gmail.com')
time.sleep(1)
driver.find_element(By.ID, 'age').send_keys('25')
time.sleep(1)
driver.find_element(By.ID, 'salary').send_keys('4000000')
time.sleep(1)
driver.find_element(By.ID, 'department').send_keys('Marketting')
time.sleep(1)
# Submit Data
driver.find_element(By.ID, 'submit').click()
time.sleep(1)