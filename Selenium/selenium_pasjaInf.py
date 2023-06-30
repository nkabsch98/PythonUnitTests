from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
import time
# not needed in newers version of Selenium: PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://pasja-informatyki.pl/")
print("Title is:"+driver.title)

try: 
    menu_icon = driver.find_element(By.CLASS_NAME, value="icon-menu-1")
    menu_icon.click()
except:
    print("Nie znaleziono ikony menu")

search_icon = driver.find_element(By.CLASS_NAME, value="icon-search")
search_icon.click()
print("1")

search = driver.find_element(By.CLASS_NAME, "form-control")
print("2")
search.send_keys("Test")
print("3")
search.send_keys(Keys.RETURN)

time.sleep(4)

try:
    postsField = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,"posts"))
    )
    posts = postsField.find_elements(By.TAG_NAME, "h2")
    for post in posts:
        header = post

finally:
    driver.close()



