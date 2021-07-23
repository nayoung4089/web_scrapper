import requests
from bs4 import BeautifulSoup

# indeed_url= "https://kr.indeed.com/jobs?q=python&limit=50&fromage=last&radius=25"

# 구성 방향:
# 나는 python이라고 입력했을 때 정보를 모두 받아오고 싶다
# 모든 페이지에 정보를 받기 위해서는 해당 a href 즉, url이 필요하다
# 보니까 달라지는 url 정보는 뒤의 숫자밖에 없다
# 그 숫자는 페이지 수 * 50이었고, 그럼 나는 페이지 수를 받아오면 된다
# 페이지 수는 가장 마지막 페이지 번호를 알아 그것을 for 통해 정렬하면 될 것 같다
# 근데 페이지 수 받았더니 내가 실제 존재하는 페이지(여기서는 1페이지)는 포함되지 않았다
# 이것을 해결하기 위해 "마지막 숫자 = 숫자의 개수"로 해주는 range를 이용해 for 구문을 작성하면 된다고 생각했다

# indeed_url= "https://kr.indeed.com/jobs?q=python&limit=50&fromage=last&radius=25"

# def extract_indeed_pages():
#   result= requests.get(indeed_url)
#   soup = BeautifulSoup(result.text, 'html.parser')
#   pagination = soup.find("div", class_="pagination")
#   pages = pagination.find_all("a")
#   spans = []
#   for page in pages[:-1]:
#     spans.append(int(page.string)),
#   max_page = spans[-1]
#   return(max_page)

limit = 50
indeed_url= f"https://kr.indeed.com/jobs?q=python&limit={limit}"

def extract_indeed_pages():
  # 우선 해당 페이지의 모든 text를 불러모아야 한다 그렇게 하기 위해서 .text 사용할 건데, 그 전에 어떤 페이지를 가져올 건지 알려주는 문구 필요함
  result = requests.get(indeed_url) 
  # 그 다음 soup 이용해서 a 관련된 태그만 찾아야 하니, 어디 텍스트에서 찾을지 soup에 입력해준다
  soup = BeautifulSoup(result.text, 'html.parser')
  pagination = soup.find("div", class_="pagination")
  # span 관련은 pagination 이라는 class 속에 있었고, 이것을 soup으로 찾은 것임
  pages = pagination.find_all("a")
  # a tag을 모두 찾았고, 그것을 보여줌
  spans = []
  # 여기다가 span 넘버를 적을 것임
  for page in pages[:-1]:
    spans.append(int(page.string)),
    # 가장 마지막 거는 숫자가 아니라 요상한 span이라서 그건 뺌. 아마 next일 듯?
    # pages에서 받은 a class 안의 span class만 string으로 숫자 보여짐. 그래서 page.string
  max_page = spans[-1]
  # 가장 최대 페이지
  return (max_page)
  # for n in range(max_page):
  #   return (f"start = {n * 50}")
  #   # 원래 spans = [2, 3, 4, 5] 였는데 max_range = 5니까 0 1 2 3 4 이렇게뜸 --> n


def extract_indeed_jobs(last_page):
  jobs= []
  for page in range(last_page):
    result = requests.get(f"{indeed_url}&start={limit * page}")
    print(result)
    # 50개씩 보여주는 걸 limit로 바꿔줘서, 최댓값을 내맘대로 지정할 수 있게 됨
    # 와 이것도 쉼표 쓰는 순간 작살남
    soup = BeautifulSoup(result.text, 'html.parser')
    result_titles = soup.find_all("h2",class_="jobTitle")
    for result_text in result_titles:
      titles = result_text.find_all("span")
      for title in titles:
        final_title = title.string
        if final_title != "new":
          # print(final_title)
          jobs.append(final_title) 
          print(final_title)

    result_etc = soup.find_all("div",class_="heading6 company_location tapItem-gutter")
    for result_company in result_etc:
      companies = result_company.find_all("span", class_="companyName")
      for company in companies:
        final_company = company.string
        # print(final_company)
        jobs.append(final_company)
        print(final_title, final_company)

    for result_location in result_etc:
      locations = result_location.find_all("div", class_="companyLocation")
      for location in locations:
        final_location = location.text
        # string으로 해주니까 +1 지역 때문에 None으로 뜸.. 그래서 text로 변경
        # print(final_location)
        jobs.append(final_location)
        return {'title': final_title, 'company': final_company, 'location': final_location}

  


