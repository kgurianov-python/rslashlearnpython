import logging

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

@FindBy
def searc():
    pass


log_format = '%(asctime)s [%(name)s]  [%(levelname)s] : %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)
logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

BASE_URL = 'https://www.amazon.com/s?k=data+science+books&ref=nb_sb_noss'

SEARCH_RESULTS_SELECTOR = (By.XPATH, "//span[@data-component-type='s-search-results']")
SINGLE_SEARCH_RESULT_SELECTOR = (By.XPATH, "//div[@data-component-type='s-search-result']")
SEARCH_RESULT_TITLE = (By.CSS_SELECTOR, 'span.a-size-base-plus.a-color-base.a-text-normal')
SEARCH_RESULT_TITLE_XPATH_STARTS_WITH = (By.XPATH, ".//span[starts-with(@class,'a-size-base-plus')]")
SEARCH_RESULT_TITLE_XPATH_CONTAINS = (By.XPATH, ".//span[contains(@class,'a-size-base-plus a-color-base a-text-normal')]")
SEARCH_RESULT_TITLE_XPATH = (By.XPATH, ".//span[@class='a-size-base-plus a-color-base a-text-normal']")

def main():
    options = Options()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    # options.add_argument("--start-fullscreen")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(BASE_URL)
        WebDriverWait(driver, 30)
        wait = WebDriverWait(driver, timeout=60, poll_frequency=2)
        wait.until(EC.presence_of_element_located(SEARCH_RESULTS_SELECTOR))
        search_results = driver.find_element(*SEARCH_RESULTS_SELECTOR)
        book_list = search_results.find_elements(*SINGLE_SEARCH_RESULT_SELECTOR)
        logger.debug(f"Books found on page: {len(book_list)=}")

        for book_item in book_list[:2]:
            book_title_element = book_item.find_element(*SEARCH_RESULT_TITLE)
            # book_title_element_xpath = book_item.find_element(*SEARCH_RESULT_TITLE_XPATH)
            logger.debug(f"Title: {book_title_element.text}")
            # logger.debug(f"{book_title_element_xpath=}")
            # logger.debug(f"Title by XPATH: {book_title_element_xpath.text}")

    except StaleElementReferenceException as e:
        logger.error(e.msg)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
