import selenium
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://simbi.io/careers/')

time.sleep(5)

jobs = driver.find_elements_by_xpath('//div[@class="angellist_jobs-job"]')

jobs_list = []

for p in range(len(jobs)):
    jobs_list.append(jobs[p].text)

print(jobs_list)