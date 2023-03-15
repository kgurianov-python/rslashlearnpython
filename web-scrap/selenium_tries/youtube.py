import logging
import random
import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

log_format = '%(asctime)s%(name)s %(levelname)s %(message)s'
logging.basicConfig(level=logging.ERROR, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

BASE_URL = "https://www.youtube.com/watch?v=91RBUmbNL1U"
youtube_button_selector_class = (By.CLASS_NAME, 'ytp-play-button')
youtube_button_selector_css = (
    By.CSS_SELECTOR, '#movie_player div.ytp-chrome-bottom div.ytp-chrome-controls div.ytp-left-controls button')

play_btn_selectors = [youtube_button_selector_class, youtube_button_selector_css]


def main():
    options = Options()
    # options.add_argument('--headless=new')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(BASE_URL)
    wait = WebDriverWait(driver, timeout=60, poll_frequency=2)
    wait.until(EC.presence_of_element_located(youtube_button_selector_class))

    for i in range(10):
        selector = play_btn_selectors[i % 2]
        logger.debug(f"Current selector: {selector=}")
        play_btn_class = driver.find_element(*selector)
        play_btn_class.click()
        time.sleep(3)

    driver.close()


if __name__ == '__main__':
    main()
