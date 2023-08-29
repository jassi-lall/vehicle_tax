from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

numberplate = "BL61LKE"
#numberplate = input("Enter numberplate: ")

driver = webdriver.Chrome()
driver.implicitly_wait(2)

url = "https://vehicleenquiry.service.gov.uk/"
driver.get(url)
sleep(5)

i = driver.find_element(By.ID, 'wizard_vehicle_enquiry_capture_vrn_vrn')
sleep(1)
i.click()
i.send_keys(numberplate)
sleep(1)
i.send_keys(Keys.RETURN)
sleep(10)

driver.find_element(By.ID, "yes-vehicle-confirm").click()
sleep(0.2)
driver.find_element(By.ID, "capture_confirm_button").click()

sleep(20)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
dd = soup.find_all('dd')
dt = soup.find_all('dt')

for i in range(len(dt)):
    print(dt[i].text, dd[i].text)