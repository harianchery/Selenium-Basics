from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()

try:
    driver.get("https://www.amazon.in")
    search=driver.find_element(By.ID,"twotabsearchtextbox")
    search.send_keys("Iphone 16")
    search.send_keys(Keys.ENTER)

    time.sleep(10)
finally:
    driver.quit()