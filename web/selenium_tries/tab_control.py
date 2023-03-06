from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.DEBUG, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

BASE_URL = 'https://www.whatismybrowser.com/detect/what-http-headers-is-my-browser-sending'
PROFILE_PATH = "C:\\Users\\kgury\\AppData\\Local\\Google\\Chrome\\User Data\\"
PROFILE_DIR = "Default"


def main():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    urls = ['https://www.google.com', 'https://www.reddit.com', 'https://stackoverflow.com/']

    try:
        driver.get(BASE_URL)
        WebDriverWait(driver, 30)
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
        for url in urls:

            driver.execute_script("window.open('about:blank');")
            windows = driver.window_handles
            driver.switch_to.window(windows[-1])
            driver.get(url)

    finally:
        driver.service.stop()


if __name__ == '__main__':
    main()
