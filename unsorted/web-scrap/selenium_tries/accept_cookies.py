"""
https://www.reddit.com/r/learnpython/comments/120h5uk/selenium_accept_cookies_throwing_error/

I am doing my first automation project using Selenium. The code goes to a webpage and accept cookies. However I get the following error from Selenium:

selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element is not clickable at point (1036, 609)

I think its do with the cookie menu popping up however i don't understand why it won't click as I do a implicit wait. Please someone help it would be greatly appreciated see code below:
"""

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Create a new Options object/instance of options
options = Options()
# Keep the Chrome browser window open after the WebDriver instance is closed using a method on the options object
options.add_experimental_option("detach", True)

# Create a new Chrome browser object/instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open webpage required
driver.get("https://super6.skysports.com/")
# driver.maximize_window()

# Wait 20 seconds for the cookies screen to show up
wait = WebDriverWait(driver, 20)

accept_cookies: WebElement = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='onetrust-accept-btn-handler']")))

# accept_cookies.click()
""" 
There is a JavaScript code in the onclick() event handler of the button, which switches current focus 
from the button to another (non-clickable) element:

    this.allowAllEventHandler = function(e) {
        void 0 === e && (e = !1),
        Wt(document).off("keydown", _r.shiftBannerFocus); # This shifts focus to another element, 
                                                             seems to the <div id="onetrust-pc-sdk" .../>
        var t = e ? "Preferences Allow All" : "Banner Accept Cookies";
        Ho.triggerGoogleAnalyticsEvent(Uo, t),
        o.allowAllEvent(!1, e),
        o.hideVendorsList()
    }

As a result, when the Selenium attempts to click,  the focus is shifted to a <div id="onetrust-pc-sdk" .. /> which is not clickable.

"""
driver.execute_script("arguments[0].click();", accept_cookies) # use JS executor to trigger click() event handler
