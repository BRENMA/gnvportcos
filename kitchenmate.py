import selenium
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=chrome_options)

driver.get('https://www.kitchenmate.com/careers#jobs')

time.sleep(5)

jobs = driver.find_elements_by_xpath('//div[@class="w-layout-grid job-grid"]')

jobs_list = []

for p in range(len(jobs)):
    jobs_list.append(jobs[p].text)

print(jobs_list)