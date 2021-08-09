import requests
from bs4 import BeautifulSoup

URL = "https://funnelytics.io/careers/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="job-row")

for job_element in job_elements:
    title = job_element.find("h3", class_="job-title")
    extra = job_element.find("div", class_="job-meta")
    links = job_element.find_all("a", class_="job-row-overlay")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}\n")
    print(title.text)
    print(extra.text)
    print()
