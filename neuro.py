import requests
from bs4 import BeautifulSoup

URL = "https://www.getneuro.ai/jobs"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="job-collection-item")

for job_element in job_elements:
    title = job_element.find("p", class_="paragraph-large")
    location = job_element.find("div", class_="detail")
    links = job_element.find_all("a", class_="job-card w-inline-block")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
    print(title.text)
    print(location.text)
    print()
