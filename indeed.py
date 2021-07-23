import requests
from bs4 import BeautifulSoup

limit = 50
URL= f"https://www.indeed.com/jobs?q=python&limit={limit}"

def get_last_page():
  result = requests.get(URL) 
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find("div", class_="pagination")
  links = pagination.find_all("a")
  pages = []
  for link in links[:-1]:
    pages.append(int(link.string)),
  max_page = pages[-1]
  return max_page

def extract_job(html):
  # title
  title = html.select_one('.jobTitle>span').string
  #와 이걸 어떻게 생각함? ㄷㄷ;; 아마 하나만 선택하라 해서 new가 선택당하지 못한듯
    
  # company  
  company = html.find("span", class_="companyName")
  final_company = company.string
  # location
  location = html.find("div", class_="companyLocation")
  final_location = location.text
  job_id = html.parent['data-jk']
  # soup를 이용해서 부모태그를 가져온 것!!
  return {'title':title, 'company':final_company, 'location':final_location,
   'link':f"https://www.indeed.com/viewjob?jk={job_id}&from=serp&vjs=3"}

def scrap_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scraping page {page}")
    result = requests.get(f"{URL}&start={page*limit}")
    soup = BeautifulSoup(result.text, 'html.parser')
    results = soup.find_all("div",class_="slider_container")
    for result_text in results:
      job = extract_job(result_text)
      jobs.append(job)
  return jobs

def get_jobs():
  last_page = get_last_page()
  jobs = scrap_jobs(last_page)
  return jobs