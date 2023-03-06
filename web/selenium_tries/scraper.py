import traceback
from typing import Any

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

div_classes = {'open': "js-symbol-open",
               'volume': "js-symbol-volume",
               'daily low': "js-symbol-header__range-price-l",
               'daily high': "js-symbol-header__range-price-r"}


def any_text_to_be_present(parent: WebElement, locator):
    def _predicate(driver):
        try:
            print(f'{parent.find_element(*locator).text=}')
            return parent.find_element(*locator).text
        except StaleElementReferenceException:
            return False

    return _predicate


def main():
    base_url = 'https://www.tradingview.com/symbols/FX-NAS100/'
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(base_url)
        # WebDriverWait(driver, 30)
        wait = WebDriverWait(driver, timeout=60, poll_frequency=10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'js-symbol-open')))
        # wait.until(any_text_to_be_present((By.CLASS_NAME, 'js-symbol-open')))
        elems = driver.find_elements(By.CLASS_NAME, div_classes['open'])
        for elem in elems:
            print(f'value : {elem.text}')

        header_container = driver.find_element(By.CLASS_NAME, 'js-header-fundamentals')
        print('waiting for text...')
        wait.until(any_text_to_be_present(header_container, (By.CLASS_NAME, div_classes['open'])), 'No text found')

        for key, val in div_classes.items():

            data = header_container.find_element(By.CLASS_NAME, val)
            # print(data)
            print(f"{key} : {data.text}")

        elems = driver.find_elements(By.CLASS_NAME, div_classes['open'])
        for elem in elems:
            print(f'value: {elem.text}')
    except Exception as e:
        traceback.print_exc()
    finally:
        driver.close()


if __name__ == '__main__':
    main()
