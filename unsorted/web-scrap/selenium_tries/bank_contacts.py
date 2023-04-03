import logging
import time

import requests
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

log_format = '%(name)s : %(levelname)s : %(asctime)s - %(message)s'
logging.basicConfig(level=logging.ERROR, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

URLS = ["https://www.jobs.bg/company/22149",
        "https://www.jobs.bg/company/unicreditbulbank",
        "https://www.jobs.bg/company/20931"]
def main():
    options = Options()
    # options.add_argument('--headless=new')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    for base_url in URLS:
        driver.get(base_url)
        wait = WebDriverWait(driver, timeout=60, poll_frequency=2)
        contacts_header_locator = (By.XPATH, "//h2[contains(text(), 'Контакти')]")
        wait.until(EC.presence_of_element_located(contacts_header_locator))
        contacts_header = driver.find_element(*contacts_header_locator)
        # GEt the parent element of the <h2>Контакти</h2>
        contacts_container = contacts_header.find_element(By.XPATH, '..')
        print(f"{contacts_container.get_attribute('outerHTML')=}")
        company_name = contacts_container.find_element(By.CLASS_NAME, 'mdc-card')
        print(f"{company_name.get_attribute('innerText')}")
        # print(f"{contacts_container.get_attribute('innerText')}")

if __name__ == '__main__':
    main()
