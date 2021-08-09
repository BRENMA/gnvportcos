import selenium
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(PATH, options=options)

driver.get('https://apply.workable.com/hockeystickco/')

time.sleep(5)

jobs = driver.find_elements_by_xpath('//div[@class="_-_-shared-ui-atoms-card-___styles__card _-_-shared-ui-atoms-card-___styles__hoverable _-_-shared-ui-atoms-card-___styles__padding-16 _-_-shared-ui-atoms-card-___styles__elevation-1 "]')

jobs_list = []

for p in range(len(jobs)):
    jobs_list.append(jobs[p].text)

print(jobs_list)