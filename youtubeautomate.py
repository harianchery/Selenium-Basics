from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()

try:
    driver.get("https://www.youtube.com")
    driver.find_element(By.NAME,"search_query").send_keys("Malayalam movie",Keys.ENTER)
    time.sleep(5)
    actualtitle=driver.title
    if actualtitle=="Malayalam movie - YouTube":
        print("Pass")
    else:
        print("Fail")
finally:
    driver.quit()
