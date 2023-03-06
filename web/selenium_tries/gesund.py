import logging
from time import sleep

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

BASE_URL = 'https://gesund.bund.de/suchen/aerztinnen-und-aerzte'

COMBO_SELECTOR = (By.ID, 'arztsuche-fachrichtung')
COMBO_OPTIONS_SELECTOR = (By.ID, 'arztsuche-fachrichtung-list')
COMBO_OPTIONS_ITEMS_SELECTOR = (By.TAG_NAME, 'input')


def build_options(options: list[WebElement]) -> dict[str, WebElement]:
    return {option.get_attribute('data-src'): option.find_element(By.XPATH, '..') for option in options}


def main():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    # options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, timeout=60, poll_frequency=1)
        wait.until(EC.presence_of_element_located(COMBO_SELECTOR))
        select_box = driver.find_element(*COMBO_SELECTOR)
        select_box.click()
        wait.until(EC.visibility_of_element_located(COMBO_OPTIONS_SELECTOR))
        options_container = driver.find_element(*COMBO_OPTIONS_SELECTOR)
        options = build_options(options_container.find_elements(*COMBO_OPTIONS_ITEMS_SELECTOR))
        logger.debug(options['Angiologie'].tag_name)
        options['Angiologie'].click()

        sleep(10)
    except StaleElementReferenceException as e:
        logger.error(e.msg)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
