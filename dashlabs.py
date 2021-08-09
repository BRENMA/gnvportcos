import requests
from bs4 import BeautifulSoup

URL = "https://careers.smartrecruiters.com/Dashlabsai"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("li", class_="opening-job job column wide-7of16 medium-1of2")

for job_element in job_elements:
    title = job_element.find("h4", class_="details-title job-title link--block-target")
    time = job_element.find("span", class_="margin--right--s")
    links = job_element.find_all("a", class_="link--block details")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}")
    print(title.text)
    print(time.text)
    print()
