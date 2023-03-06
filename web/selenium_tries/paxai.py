import logging
import os
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

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.ERROR, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

BASE_URL = 'https://pixai.art/@solomoncyj/tasks'


login_user_selector = (By.ID, "email-input")
login_pwd_selector = (By.ID, "password-input")
login_btn_selector = (By.XPATH, "//button[contains(text(), 'Login')]")
container_selector = (By.CLASS_NAME, 'py-4')
container_selector_internal = (By.CLASS_NAME, 'py-4')
images_selector = (By.XPATH, "//div[@role='button']")
modal_dialog_selector=(By.XPATH, "//div[@role='dialog']")
next_selector = (By.XPATH, "//*[contains(text(), 'next')]")


def main():
    options = Options()
    login = input("Login:\t")
    password = input("Password:\t")
    # options.add_argument('--headless=new')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(BASE_URL)
    WebDriverWait(driver, 10)
    wait = WebDriverWait(driver, timeout=60, poll_frequency=2)
    wait.until(EC.presence_of_element_located(login_btn_selector))
    driver.find_element(*login_user_selector).send_keys(login)
    driver.find_element(*login_pwd_selector).send_keys(password)
    driver.find_element(*login_btn_selector).click()

    next_page_exists = True
    while next_page_exists:
        logger.debug('next page')
        wait.until(EC.presence_of_element_located(container_selector))
        container = driver.find_element(*container_selector).find_element(*container_selector_internal)

        container_wait = WebDriverWait(container, timeout=60, poll_frequency=2)

        container_wait.until(EC.presence_of_element_located(images_selector))
        # print(f"{container.get_attribute('outerHTML')=}")
        images_list = container.find_elements(*images_selector)

        download_counter = 0
        while os.path.exists(filename := f'download-{download_counter:05}.avif'):
            download_counter += 1

        logger.debug(f"{len(images_list)=}")
        for image_tile in images_list:
            image_tile.click()

            modal_locator = driver.find_element(*modal_dialog_selector)
            img_wait = WebDriverWait(modal_locator, timeout=60, poll_frequency=2)

            img_locator = (By.TAG_NAME, "img")
            img_wait.until(EC.presence_of_element_located(img_locator))
            img = modal_locator.find_element(*img_locator)

            image_url = img.get_attribute('src')

            logger.debug(f"{image_url}")

            img_data = requests.get(image_url).content
            with open(filename, 'wb') as handler:
                handler.write(img_data)
                download_counter += 1
                filename = f'download-{download_counter:05}.avif'
            webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(1)

        container_wait.until(EC.presence_of_element_located(next_selector))
        if next_page := container_wait.until(EC.element_to_be_clickable(next_selector)):
            try:
                next_page.click()
            except ElementClickInterceptedException as e:
                next_page_exists = False

    time.sleep(10)


if __name__ == '__main__':
    main()
