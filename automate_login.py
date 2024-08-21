from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime, timedelta
import time

# Chrome 드라이버 경로 설정
chrome_driver_path = 'C:/Users/sanghojeong9210/Downloads/chromedriver_win64/chromedriver.exe'

# Selenium WebDriver 설정
service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)

# Open the webpage
driver.get("https://magihr.miraeasset.com/login")

# Find the element with id 'username' and input the username
username_element = driver.find_element(By.ID, "username")
username_element.send_keys("A01696")

# Find the element with id 'password' and input the password
password_element = driver.find_element(By.ID, "password")
password_element.send_keys("Ajfxl@9210!@")

# Find the login button with id 'btnLogin' and click it
login_button = driver.find_element(By.ID, "btnLogin")
login_button.click()

# Wait for the page to load after login
driver.implicitly_wait(10)  # Implicit wait to allow time for the page to load

# Find the button with id 'wStartBtn' and click it
start_button = driver.find_element(By.ID, "wStartBtn")
start_button.click()

# Add a wait to observe the result (optional)
import time
time.sleep(5)

# Close the browser
driver.quit()