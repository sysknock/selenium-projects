from selenium import webdriver
import time
# Initialize the browser (ensure you have the correct driver installed)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")


search_box = driver.find_element("name", "q")
time.sleep(5)
search_box.send_keys("Selenium Python")
time.sleep(5)
search_box.submit()
time.sleep(10)
driver.quit()

"""
search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium Python")
search_box.submit()

search_box = driver.find_element("name", "q")
search_box.send_keys("Selenium Python")
# Locate the search button using its name attribute "btnK"
search_button = driver.find_element("name", "btnK")
search_button.click()
"""