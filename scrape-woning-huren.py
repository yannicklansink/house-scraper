import sys
import selenium
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.common.keys import Keys

print("start program")

load_dotenv()

# Now you can access your password as an environment variable
password = os.getenv('USER_PASSWORD')
username = os.getenv('USER_USERNAME')

print(f"Username: {username}")
print(f"Password: {password}")


driver = webdriver.Chrome()

driver.get("https://www.woninghuren.nl/inloggen?previousPage=https%3A%2F%2Fwww.woninghuren.nl%2Fmijn-omgeving%2Fmijn-zoektocht%2Faangeboden-woningen&cHash=e7a3784682d38669bfbb8f283b2e2d05")

# Wait for the page to load
time.sleep(2)

# Define a wait
wait = WebDriverWait(driver, 10)

# Wait until the cookies acceptance button is clickable and click it
cookie_accept_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Cookies accepteren')]")))
cookie_accept_button.click()

# Then wait a moment for the cookie banner to disappear
time.sleep(2)

# Define a wait
wait = WebDriverWait(driver, 10)

# Wait until the username and password fields are visible
username_field = wait.until(EC.visibility_of_element_located((By.ID, "username")))
password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))

# Enter the username and password using JavaScript
driver.execute_script('angular.element(document.getElementById("username")).scope().form.data.username = arguments[0];', username)
driver.execute_script('angular.element(document.getElementById("password")).scope().form.data.password = arguments[0];', password)

# Trigger an input event to inform AngularJS about the change
driver.execute_script('angular.element(document.getElementById("username")).scope().$apply();')
driver.execute_script('angular.element(document.getElementById("password")).scope().$apply();')

# Locate the submit button and click it
submit_button = driver.find_element_by_xpath("//input[@type='submit'][@value='Inloggen']")
submit_button.click()
