from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

# 데이터를 받을 리스트
title_t = []
company_t = []
link_t = []

# IT개발·데이터 직무 크롤링
url = 'https://www.saramin.co.kr/zf_user/search?cat_mcls=2&company_cd=0%2C1%2C2%2C3%2C4%2C5%2C6%2C7%2C9%2C10&panel_type=&search_optional_item=y&search_done=y&panel_count=y'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
request = Request(url, headers=headers)
response = urlopen(request)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# 제목
title = soup.select('#recruit_info_list > div.content > div > div.area_job > h2 > a > span')
for t in title:
    title_t.append(t.text)

# 회사명
company = soup.select('#recruit_info_list > div.content > div > div.area_corp > strong > a > span')
for t in company:
    company_t.append(t.text)
    
# 채용 공고 링크
link = soup.select('#recruit_info_list > div.content > div > div.area_job > h2 > a')
'https://www.saramin.co.kr' + link[0]['href']
for l in link:
    link_t.append('https://www.saramin.co.kr' + l['href'])

