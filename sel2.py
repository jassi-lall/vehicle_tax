"""
TODO: optimise sleep() times. They are currently quite random
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup

numberplate = "BL61LKE"
#numberplate = input("Enter numberplate: ")

driver = webdriver.Firefox()
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

result = driver.page_source
driver.close()

print(BeautifulSoup(result, 'html.parser').prettify())