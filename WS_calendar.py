import requests, ssl
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context

def get_calendar():
    main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=2021&ymonth=12&mzcode=K00M0409&gubun=UN'
    res = requests.get(main_url,verify=False)
    soup = BeautifulSoup(res.content, 'lxml')
    date_t = []
    day_t = []

    date = soup.select('#month_iljung > dl > dd.date_info > span')
    for t in date:
        date_t.append(t.text)

    day = soup.select('#month_iljung > dl > dd.day_info > span')
    for t in day:
        day_t.append(t.text)
    
    return [date_t,day_t]