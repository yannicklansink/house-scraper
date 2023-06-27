import sys
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print("start program")

driver = webdriver.Chrome()

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

time.sleep(2)

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

print(submit_button)






