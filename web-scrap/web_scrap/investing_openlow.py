import logging

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.ERROR, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)


VALUES_CONTAINER_LOCATOR = (By.XPATH, '//dl[@data-test="key-info"]')
DIV_CLASSES = {'open': (By.XPATH, '//dd[@data-test="open"]'),
               'low': (By.XPATH, '//dd[@data-test="dailyRange"]/span[1]/span[1]'),
               'high': (By.XPATH, '//dd[@data-test="dailyRange"]/span[3]/span[1]')}


def main():
    base_url = 'https://www.investing.com/indices/us-30-futures'
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    values_dict = {}
    try:
        driver.get(base_url)
        wait = WebDriverWait(driver, timeout=60, poll_frequency=2)
        wait.until(EC.presence_of_element_located(VALUES_CONTAINER_LOCATOR))
        header_container = driver.find_element(*VALUES_CONTAINER_LOCATOR)
        for key, val in DIV_CLASSES.items():
            data = header_container.find_element(*val)

            values_dict.update({key : data.text})
        print(values_dict)

    except Exception as e:
        logger.info(e)
    finally:
        driver.close()


main()
