from bs4 import BeautifulSoup
import requests



URL = "https://stay22.breezy.hr/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("li", class_="position")

for job_element in job_elements:
    title = job_element.find("h2").text
    location = job_element.find("span").text
    links = job_element.find_all("a")
    for link in links:
        link_url = link["href"]
    print(title)
    print(location)
    print(f"Apply Here: {link_url}")
    print()