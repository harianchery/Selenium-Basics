from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()

try:
    driver.get("http://127.0.0.1:5500/index.html")
    check_element=driver.find_element(By.TAG_NAME,"h1")
    if check_element.text.strip()=="FISAT":
        print("PASSED")
        driver.find_element(By.NAME,"fname").send_keys("Hari")
        time.sleep(3)
    else:
        print("FAILED")

finally:
    driver.quit()