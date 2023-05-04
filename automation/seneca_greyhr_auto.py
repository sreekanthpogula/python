from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# create a new Firefox browser instance
browser = webdriver.Firefox()

# navigate to the website login page
browser.get("https://senecaglobal.greythr.com/v3/portal/ess/home")

# enter your username and password in the login form
username = browser.find_element_by_id("loginName")
password = browser.find_element_by_id("password")
username.send_keys("your_username")
password.send_keys("your_password")

# submit the login form
password.send_keys(Keys.RETURN)

# wait for the page to load
time.sleep(5)

# navigate to the logout page
browser.get("")

# close the browser window
browser.quit()
