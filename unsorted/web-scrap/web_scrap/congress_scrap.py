import pandas as pd
from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'https://www.congress.gov/search?q=%7B%22source%22%3A%22legislation%22%7D'


def main():
    options = Options()
    # options.add_argument('--headless=new')
    options.add_argument('--headless')
    options.add_argument("no-sandbox")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    try:
        driver.get(BASE_URL)
        print(driver.find_element(By.TAG_NAME, 'html').text)
        wait = WebDriverWait(driver, timeout=60, poll_frequency=5)
        wait.until(EC.presence_of_element_located((By.ID, 'main')))

        search_container = driver.find_element(By.ID, 'main')
        search_results = search_container.find_elements(By.XPATH,
                                                        "//li[@class='expanded']//span[@class='result-heading']")

        print(f'Number of titles found: {len(search_results)}')
        # df = pd.DataFrame(columns=['Title'])
        titles = {'Titles': [search_result.text for search_result in search_results]}
        df = pd.DataFrame.from_dict(titles)
        print(df)

    except TimeoutException:
        print("Timed out waiting for data")
    except NoSuchElementException as e:
        print(e.msg)
    finally:
        driver.close()


if __name__ == '__main__':
    main()
