# Using Python Selenium Automation and the URL https://www.saucedemo.com/
# display the Cookie created before login and after login in the console.
# After you login into the dashboard of the Zen portal kindly do the logout also.
# Verify that the cookies are being generated during the Login process.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

opt = webdriver.ChromeOptions()
opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)

# Cookies are small pieces of data stored by a web browser on a user's device,
# containing information about the user or their interaction with a website.
# saucedemo

driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com/")

try:
    cookies_found_before_login = []
    print("No cookies found before login in 'saucedemo'")
except:
    cookies_found_before_login = driver.get_cookies()
    print("cookies_found_before_login_saucedemo:", cookies_found_before_login)

# login
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

username_input.send_keys("standard_user")
password_input.send_keys("secret_sauce")
login_button.click()

try:
    cookies_found_after_login = []
    print("No cookies found after login in 'saucedemo'")
except:
    cookies_found_after_login = driver.get_cookies()
    print("cookies_found_after_login_saucedemo:", cookies_found_after_login)

driver.find_element(By.XPATH,"//div[@class='bm-burger-button']/button").click()
driver.find_element(By.LINK_TEXT,"Logout").click()

# Zen portal

driver.switch_to.new_window("tab")
driver.get("https://www.zenclass.in/login")

try:
    cookies_found_before_login = []
    print("No cookies found before login in 'Zen portal'")
except:
    cookies_found_before_login = driver.get_cookies()
    print("cookies_found_before_login_zen_portal:", cookies_found_before_login)

# login
username_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")

username_input.send_keys("nabila2203@gmail.com")
password_input.send_keys("Nabela@24")
login_button.click()

try:
    cookies_found_after_login = []
    print("No cookies found after login in 'Zen portal'")
except:
    cookies_found_after_login = driver.get_cookies()
    print("cookies_found_after_login_zen_portal:", cookies_found_after_login)

driver.find_element(By.XPATH,"//img[@class='profileIcon']").click()
driver.find_element(By.XPATH,"//button[text()='Logout']").click()

driver.quit()
