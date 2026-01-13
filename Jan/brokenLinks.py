from http.client import responses

import requests
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import *
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
now = datetime.now()

options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
options.accept_insecure_certs = True

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
wait = WebDriverWait(driver, 30)


driver.get("https://www.eddymens.com/blog/page-with-broken-pages-for-testing-53049e870421")

links  =driver.find_elements("tag name","a")
print(len(links))
try:
    for link in links:
        url = link.get_attribute("href")
        if url:
            response = requests.head(url)
            if response.status_code >= 400:
                print(f"Broken Links :{url} - status code :{response.status_code}")
            else:
                print(f"valid link :{url}")
    time.sleep(5)
except:
    print("try failed")