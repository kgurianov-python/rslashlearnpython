import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")

try:
    driver.get("http://www.google.com")
    input_element = driver.find_element(By.NAME, 'q')
    input_element.send_keys("only 4 links")
    input_element.submit()
    results = driver.find_elements(By.CLASS_NAME, 'g')
    for result in results[:4]:
        link = result.find_element(By.TAG_NAME, 'a')
        ActionChains(driver).move_to_element(link).\
            key_down(Keys.CONTROL).\
            click(link).\
            key_up(Keys.CONTROL).\
            perform()

except Exception as e:
    print(e)
    driver.close()

for handle in driver.window_handles:
    driver.switch_to.window(handle)
    print(f'Located window: {driver.title} {driver.current_url}')


windows = driver.window_handles
driver.switch_to.window(windows[-1])
time.sleep(2)
driver.get("http://www.google.com")

time.sleep(10)