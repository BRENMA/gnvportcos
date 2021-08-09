import selenium
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://www.voiceflow.com/about#Jobs')

time.sleep(5)

jobs = driver.find_elements_by_xpath('//a[@class="link-block-17 w-inline-block"]')

jobs_list = []

for p in range(len(jobs)):
    jobs_list.append(jobs[p].text)

print(jobs_list)