import requests
from bs4 import BeautifulSoup

def scrape_jobs(keyword="python"):
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("tr", class_="job")
    job_list = []

    for job in jobs:
        try:
            title = job.find("h2").text.strip()
            company = job.find("h3").text.strip()
            link = "https://remoteok.com" + job.find("a", class_="preventLink")["href"]
            job_list.append({"title": title, "company": company, "link": link})
        except:
            continue

    return job_list