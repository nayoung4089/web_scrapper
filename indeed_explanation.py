import requests
# url을 쉽게 import하기 위해 requests를 깔아줌
from bs4 import BeautifulSoup
# requests에서 text를 가져왔을 때 효율적인 함수 사용하기 위해 깔아줌

indeed_url= "https://kr.indeed.com/jobs?q=python&limit=50&fromage=last&radius=25"

def extract_indeed_pages():
  indeed_result= requests.get(indeed_url)
# requests에서 get이라는 함수를 가져왔으니 request.get 쓴 거.
# 앞에 예시로 써진 r = indeed_result임. 이렇게 이름 바뀌는 거 가능

# print(indeed_result)
# 이러면 [200]이 뜨는데 이건 ok라는 의미임
# print(indeed_result.text)
# ->모든 html이 로딩됨
# 이때 html에서 원하는 단어 등을 잘 찾게 도와주는 라이브러리가 beautifulsoup.

  indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')
# print(indeed_soup)
# 하면 indeed_result.text에서 나왔던 html이 정상적으로 콘솔창에 촤르륵 입력됨.
# 결과는 print(indeed_result.text)와 같은 상황

  pagination = indeed_soup.find("div", class_="pagination")
  pages = pagination.find_all("a")
  spans = []
# print(pages)
  for page in pages[:-1]:
  # [:-1]은 int 시 마지막 요상한 태그가 int로 변환 안된다고 에러뜨는 것을 방지하기 위해!!
  # for은 모든 items들을 일렬정렬하는 역할 한다고 배움!!
  # 그래서 찾은 모든 a href 중에서 span을 일렬정렬 하기 위해 이렇게 씀
  # print(page.find("span"))
    spans.append(int(page.string)),
  # page.find("span") = page, 왜냐하면 어차피 a href 안에 string이 span에 포함되어 있기 때문에 굳이 span이라고 한정지어줄 필요가 없음
  # .string을 붙이는 순간 str만 가져옴 즉, 우리가 필요한 숫자~~
  # '2','3','4','5' 이렇게 불러짐
    print(spans[-1]) 
# 가장 마지막 페이지의 숫자를 알게 됨

  max_page = spans[-1]

  for n in range(max_page):
  # max_page의 개수 알고 싶다! 그리고 그것을 item별로 정리
  # print(n)
  # 이러면 0 1 2 3 4 세로정렬됨
  # 원래는 2 3 4 5는데, 5라는 숫자 맞게 range가 생겼기 때문에 0부터 시작
    print(f"start={n * 50}"),