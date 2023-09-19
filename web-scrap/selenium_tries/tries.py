"""
A simple template for selenium-based scripts
"""
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
# options.add_argument('--headless=new')
# options.add_argument('--disable-gpu')  # Last I checked this was necessary.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

if __name__ == '__main__':
    driver.get('https://inventwithpython.com')
    try:
        elem = driver.find_element(By.CLASS_NAME, 'card-img-top')
        print(f'found {elem.tag_name} element with that class name!')
    except NoSuchElementException:
        print('Was not able to find an element with that name')
