import selenium
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=chrome_options)

driver.get('https://www.workatastartup.com/companies/datafold')

jobs = driver.find_elements_by_xpath('//div[@class="job-group"]')

jobs_list = []

for p in range(len(jobs)):
    jobs_list.append(jobs[p].text)

print(jobs_list)