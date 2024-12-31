from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    search=driver.find_element(By.NAME,"q")
    search.send_keys("Fisat")
    search.send_keys(Keys.ENTER)
    time.sleep(10)
    
finally:
    driver.quit()
