from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
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

BASE_URL = 'https://www.saucedemo.com/'

LOCATORS = {'login': {'user_name_field': (By.ID, 'user-name'),
                      'password_field': (By.ID, 'password'),
                      'login-button': (By.ID, 'login-button')},
            'inventory': {'container': (By.ID, 'inventory_container'),
                          'inventory_item': (By.CLASS_NAME, 'inventory_item'),
                          'inventory_item_name': (By.CLASS_NAME, 'inventory_item_name'),
                          'inventory_item_desc': (By.CLASS_NAME, 'inventory_item_desc'),
                          'add_to_cart_button': (By.XPATH, "//button[starts-with(@id, 'add-to-cart')]")}}


def do_login(driver: WebDriver) -> None:
    login_locators = LOCATORS['login']

    driver.find_element(*login_locators['user_name_field']).send_keys('standard_user')
    driver.find_element(*login_locators['password_field']).send_keys('secret_sauce')
    driver.find_element(*login_locators['login-button']).click()
    # WebDriverWait(driver, 30)


def do_add_all_products(driver: WebDriver) -> None:
    inventory_locators = LOCATORS['inventory']

    # Retrieve the container, which groups all inventory items -
    # in this case an outer <div/> with id='inventory_container'
    container = driver.find_element(*inventory_locators['container'])

    # Retrieve all inventory items inside the container

    items = container.find_elements(*inventory_locators['inventory_item'])
    logger.debug(f'Items: {len(items)}')

    # Iterate through each inventory item and click button "ADD TO CART"
    for item in driver.find_element(*inventory_locators['container']).find_elements(
            *inventory_locators['inventory_item']):
        item_name = item.find_element(*inventory_locators['inventory_item_name']).text
        logger.info(f"Item Name: {item_name}")

        item_description = item.find_element(*inventory_locators['inventory_item_desc']).text

        logger.info(f"Item Description {item_description}")

        button = item.find_element(*inventory_locators['add_to_cart_button'])
        button.click()
        time.sleep(1)


def main():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(BASE_URL)
        WebDriverWait(driver, 30)
        do_login(driver)
        # time.sleep(10)
        logger.debug('================================ START CLICKING ============================')
        do_add_all_products(driver)
        time.sleep(10)
    except StaleElementReferenceException as e:
        logger.error(e.msg)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
