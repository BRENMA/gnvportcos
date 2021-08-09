import selenium
PATH = "C:\Program Files (x86)\chromedriver.exe"
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=chrome_options)

driver.get('https://coinchange.io/careers')

html = driver.page_source

title = driver.find_elements_by_xpath('//*[@data-field-width-value="330"]')
description = driver.find_elements_by_xpath('//*[@data-field-width-value="270"]')

title_list = []
description_list = []

for p in range(len(title)):
    title_list.append(title[p].text)

for p in range(len(description)):
    description_list.append(description[p].text)

print(title_list)
print()
print(description_list)