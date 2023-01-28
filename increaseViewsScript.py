from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://github.com/GITHUB_USERNAME"

while 1:
    driver.get(url)
    time.sleep(1)
