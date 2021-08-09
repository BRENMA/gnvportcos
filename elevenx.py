import requests
from bs4 import BeautifulSoup

URL = "https://eleven-x.com/careers/"
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, "html.parser")

job_elements = soup.find_all("div", class_="row career-collapse")

for job_element in job_elements:
    title = job_element.find("p", class_="career-title text-left") 
    info = job_element.find("div", class_="row d-flex align-items-center pb-4")
    meta = info.find("div", class_="col-md-9")
    links = job_element.find_all("a", class_="btn-apply scroll-to")
    for link in links:
        link_url = link["href"]
        print(f"Apply here: {link_url}")
    print(title.text)
    print(meta.text)
    print()
