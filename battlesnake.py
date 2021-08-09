import requests
from bs4 import BeautifulSoup

URL = "https://play.battlesnake.com/careers/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="card-body")

for job_element in job_elements:
    title = job_element.find("h3", class_="text-primary")
    company = job_element.find("p")
    print(title.text)
    print(company.text)
    print()

for job_link in job_elements:
    links = job_link.find_all("a")
for link in links:
    link_url = link["href"]
    print({link_url})