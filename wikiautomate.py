from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
try:
    driver.get("https://www.wikipedia.org")
    driver.find_element(By.ID,"searchInput").send_keys("India",Keys.ENTER)
    time.sleep(5)
    actualtitle=driver.title
    if actualtitle=="India - Wikipedia":
        print("Passed")
    else:
        print("Failed")

    driver.back()
    time.sleep(3)
    tit=driver.title
    if tit=="Wikipedia":
        print("PASS")
    else:
        print("FAIL")


finally:
    driver.quit()

