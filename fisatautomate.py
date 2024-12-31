from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()

try:
    driver.get("https://www.fisat.ac.in")
    driver.find_element(By.ID,"menu-item-dropdown-4054").click()
    driver.find_element(By.ID,"menu-item-dropdown-4059").click()
    driver.find_element(By.ID,"menu-item-dropdown-4144").click()
    actualtitle=driver.title
    if actualtitle=="Computer Applications | FISAT | Federal Institute of Science And Technology":
        print("Passed")
    else:
        print("Failed")
    
    time.sleep(10)
finally:
    driver.quit()