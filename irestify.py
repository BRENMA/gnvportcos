import selenium
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=chrome_options)

driver.get('https://irestify.com/join-us/')

time.sleep(5)

jobs = driver.find_elements_by_xpath('//div[@class="et_pb_column et_pb_column_1_2 et_pb_column_13  et_pb_css_mix_blend_mode_passthrough et-last-child"]')

jobs_list = []

for p in range(len(jobs)):
    jobs_list.append(jobs[p].text)

print(jobs_list)