from selenium import webdriver
import time

PATH = "C:\webdrivers\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://popcat.click/")
# Any orders under this line
main = driver.find_element_by_id("app")

value = True
while (value):
    main.click()


time.sleep(5)
driver.quit()
