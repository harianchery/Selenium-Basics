from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
try:
    driver.get("https://www.flipkart.com")

    driver.find_element(By.NAME,"q").send_keys("Iphone 16",Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.ID,"productRating_LSTMOBH4DQFG8NKFRDYKOOGZ6_MOBH4DQFG8NKFRDY_").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,"OGrnIL").click()
    time.sleep(3)



finally:
    driver.quit()
