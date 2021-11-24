import requests, ssl
from bs4 import BeautifulSoup
ssl._create_default_https_context = ssl._create_unverified_context

def WS_calendar(yyear,ymonth):
    if yyear == None:
        main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=2021&ymonth=%d&mzcode=K00M0409&gubun=UN'%ymonth
    else:
        main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=20%d&ymonth=%d&mzcode=K00M0409&gubun=UN'%yyear%ymonth
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
    
    return date_t,day_t