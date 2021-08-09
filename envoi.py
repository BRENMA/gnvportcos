import requests
from bs4 import BeautifulSoup

URL = "https://envoi.breezy.hr/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("li", class_="position transition")

for job_element in job_elements:
    title = job_element.find("h2")
    extra = job_element.find("ul", class_="meta")
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}")
    print(title.text)
    print(extra.text)
    print()