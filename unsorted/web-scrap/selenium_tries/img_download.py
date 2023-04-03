import logging
import os
import shutil
import time

import requests
from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

BASE_URL = 'google.com'


def main():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://upload.wikimedia.org/wikipedia/commons/1/15/Cat_August_2010-4.jpg")
        time.sleep(0.5)
        file_path = '../../python_external_modules/tkinter_tries/background2.jpg'
        img_content1 = driver.find_element(By.TAG_NAME, "img").get_attribute('src')
        logger.debug(img_content1)
        img_content = requests.get(img_content1, stream=True)
        logger.debug(type(img_content1))
        logger.debug(img_content)
        r = img_content
        # Check image
        logger.debug(r.status_code)
        if r.status_code == 200:

            # Preventing the downloaded image’s size from being zero.
            r.raw.decode_content = True
            logger.debug(f'Request result raw: {r.raw=}')
            # Open a local file
            with open(file_path, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            logger.debug(f'Image successfully Downloaded: {file_path}')
        else:
            logger.debug('Image Couldn\'t be retrieved')

        logger.debug(os.listdir())

    except StaleElementReferenceException as e:
        logger.error(e.msg)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
