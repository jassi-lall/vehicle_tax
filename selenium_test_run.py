"""
Basic test run of selenium on google
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


search_term = "ice cream"

driver = webdriver.Firefox()
driver.implicitly_wait(3)

url = "https://www.google.co.uk/"
driver.get(url)

# Reject cookies
button = driver.find_element(By.ID, "W0wltc")
button.click()

# Search for term
search_bar = driver.find_element(By.ID, "APjFqb")
search_bar.send_keys(search_term)
sleep(1) #required
search_bar.send_keys(Keys.RETURN)
sleep(3)

driver.close()