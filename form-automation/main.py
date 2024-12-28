# The goal is to automate filling out and submitting a form on a web application. 
# We'll demonstrate the process using a login form.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.browserstack.com/users/sign_in")

username_field = driver.find_element(By.ID, "user_email_login")
username_field.send_keys("abc@gmail.com")
time.sleep(5)
# Locate and fill the password field
password_field = driver.find_element(By.ID, "user_password")
password_field.send_keys("your_password")
time.sleep(5)
login_button = driver.find_element(By.ID, "user_submit")
login_button.click()
time.sleep(5)

actualUrl="https://live.browserstack.com/dashboard"
expectedUrl= driver.current_url
assert expectedUrl==actualUrl, "The actual and expected url arent the same."