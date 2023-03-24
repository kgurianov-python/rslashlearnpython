"""
https://www.reddit.com/r/learnpython/comments/120evlj/how_can_i_get_all_the_info_of_each_of_these_popup/

link: https://macarte.ign.fr/carte/bcd30790c959c1f17308ab5b797ae318/carte_des_bivouacs_du_GR10

i have no idea how to even get that data in the first place on these kind of web elements. In the html there's only 1
line that updates dynamically, without it sending post or get requests in the network tab.
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = 'https://macarte.ign.fr/carte/bcd30790c959c1f17308ab5b797ae318/carte_des_bivouacs_du_GR10'
options = Options()

options.add_argument('--headless=new')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(BASE_URL)
result = driver.execute_script("return symfony.data.layers[4].features")
for item in result[:10]:
    print(item['popupcontent'])
