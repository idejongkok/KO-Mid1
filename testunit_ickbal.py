
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(2)
driver.get('https://demoqa.com/webtables')

def apus(x):
    for i in range(x):
        hapus = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div/div[7]/div/span[2]')
        hapus.click()

def test_apus():
    apus(2)
    element = driver.find_element(By.XPATH,'//*[@id="delete-record-3"]')
    assert element.is_displayed
    
def test_apus2():
    apus(3)
    element = driver.find_element(By.XPATH,'//*[@id="delete-record-3"]')
    assert element.is_displayed(False)

apus(3)

namaDepan =['ickbal','ackbar','Nita']
namaBelakang =['pebri','Fadhilah','Syafitri']
age =['23','22','23']
email =['ickbalpebri@gmail.com','ackbar321@gmail.com','nita12@gmail.com']
salary =['30','20','20']
dapartment=['IT','IT','Admin']

for i in range(3):
    buttonAdd = driver.find_element(By.XPATH,'//*[@id="addNewRecordButton"]')
    buttonAdd.click()
    nama_Depan = driver.find_element(By.XPATH,'//*[@id="firstName"]').send_keys(namaDepan[i])
    nama_Belakang = driver.find_element(By.XPATH,'//*[@id="lastName"]').send_keys(namaBelakang[i])
    email1 = driver.find_element(By.XPATH,'//*[@id="userEmail"]').send_keys(email[i])
    age2 = driver.find_element(By.XPATH,'//*[@id="age"]').send_keys(age[i])
    salary2 = driver.find_element(By.XPATH,'//*[@id="salary"]').send_keys(salary[i])
    dapartment2 = driver.find_element(By.XPATH,'//*[@id="department"]').send_keys(dapartment[i])
    buttonSumbit = driver.find_element(By.XPATH,'//*[@id="submit"]')
    buttonSumbit.click()
sleep(10)