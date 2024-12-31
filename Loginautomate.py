from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()

try:
    driver.get("http://10.0.16.206:5501/test.html")
    driver.find_element(By.NAME,"username").send_keys("admin")
    driver.find_element(By.NAME,"password").send_keys("12345")
    driver.find_element(By.ID,"login_button").click()
    actualtitle=driver.title
    time.sleep(1)

    if actualtitle=="Dashboard":
        print("Pass")
    else:
        print("Fail")

    driver.back()
    driver.find_element(By.NAME,"username").send_keys("adin")
    driver.find_element(By.NAME,"password").send_keys("2345")
    driver.find_element(By.ID,"login_button").click()
    check=driver.find_element(By.ID,"error_message")
    #print(check.text)
    time.sleep(1)
    if check.text=="Invalid username or password":
        print("Passed")
    else:
        print("Failed")
finally:
    driver.quit()



