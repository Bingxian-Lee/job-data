
import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
    headers = {
        '<insert user agent>'}
    url = f"<insert job site>"
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return(soup)


def transform(soup):
    table_data = soup.find_all('td', class_="resultContent")
    jd_data = soup.find_all('div', class_="result-footer")

    for item in table_data:
        title = item.find('a').text.strip()

        try:
            company = item.find('span', class_='companyName').text.strip()
        except:
            company = ' '

        try:
            salary = item.find('div', class_='salaryOnly').text.strip()
        except:
            salary = ' '

        job = {
            'title': title,
            'company': company,
            'salary': salary,
            'jd': None
        }
        jobList.append(job)

    for desc in jd_data:
        try:
            jobDesc = desc.find(
                'div', class_='job-snippet').text.replace('\n', ' ')
        except:
            jobDesc = ' '

        jd.append(jobDesc)

    for i in range(len(jobList)):
        jobList[i]['jd'] = jd[i]

    return


jd = []
jobList = []

for i in range(0, 50):
    c = extract(i)
    transform(c)

df = pd.DataFrame(jobList)
print(df.head())
df.to_csv('jobs.csv')
