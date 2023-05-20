import logging
import time
from logging import Logger

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger: Logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

BASE_URL = 'https://shop.tesla.com/en_ie/product/blue-adapter---16a_32a-'


def main():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(BASE_URL)

        # get the div container displayed on desktop browsers
        desktop_view_container = driver.find_element(By.CLASS_NAME, 'desktop-product-container')

        # get the div container for the product side panel
        product_container_side = WebDriverWait(desktop_view_container, 10, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'product__container__side')))

        # get the product style selector
        select_style = Select(WebDriverWait(product_container_side, 10, 1).until(EC.presence_of_element_located(
            (By.ID, 'product-color-select-desktop'))))

        stock_notification_container: WebElement = WebDriverWait(desktop_view_container, 10, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'stockNotification_container')))
        logger.debug(f"{stock_notification_container.is_displayed() = }")

        time.sleep(5)
        # loop through available options and check if the item style is in stock
        for option in select_style.options[1:]:
            logger.debug(f"Choosing option \"{option.text}\"")
            select_style.select_by_visible_text(option.text)

            time.sleep(0.5)
            stock_notification_container: WebElement = WebDriverWait(desktop_view_container, 10, 1).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'stockNotification_container')))
            logger.debug(f"{stock_notification_container.is_displayed() = }")

    except StaleElementReferenceException as e:
        logger.error(e.msg)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
