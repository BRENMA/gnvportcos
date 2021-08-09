import requests
from bs4 import BeautifulSoup

URL = "https://www.cuboh.com/careers#Open-Positions"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="w-dyn-item")

for job_element in job_elements:
    title = job_element.find("h6", class_="job-title")
    time = job_element.find("div",class_="text-block-27")
    location = job_element.find("div",class_="text-block-28")
    links = job_element.find_all("a", class_="card bg-offset-white career-link w-inline-block")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}")
    print(title.text)
    
    if job_element.find("div",class_="text-block-27"):
        print(time.text)

    if job_element.find("div",class_="text-block-27"):
        print(location.text)    
    
    print()