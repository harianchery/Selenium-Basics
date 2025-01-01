from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver=webdriver.Chrome()

try:
    driver.get("https://www.google.com/")
    driver.maximize_window()
    time.sleep(2)
    actualTitle=driver.title
    if actualTitle=="Google":
        print("Test pass")
        searchBox=driver.find_element(By.XPATH,"//*[@id='APjFqb']")
        searchBox.send_keys("Iphone")
        searchBox.send_keys(Keys.ENTER)
        

        WebDriverWait(driver,40).until(expected_conditions.presence_of_element_located((By.ID,"search")))
        searchResult=driver.find_elements(By.XPATH,"//h3[contains(@class,'LC20lb')]")
        print(searchResult)
        print(len(searchResult))
        for i in range(0,len(searchResult)):
            print(searchResult[i].text)
        
    
    else:
        print("Test failed")

finally:
    driver.quit()