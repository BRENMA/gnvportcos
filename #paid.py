import selenium
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
driver = webdriver.Chrome(PATH)

driver.get('https://hashtagpaid.com/company#careers')

jobs = driver.find_elements_by_xpath('//div[@class="single-role"]')

jobs_list = []

for p in range(len(jobs)):
    jobs_list.append(jobs[p].text)

print(jobs_list)