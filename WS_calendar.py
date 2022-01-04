import requests, ssl
from bs4 import BeautifulSoup
from datetime import datetime
ssl._create_default_https_context = ssl._create_unverified_context

def WS_calendar(yyear,ymonth):
    if (ymonth == None) and (yyear == None):
        yyear,ymonth = int(datetime.today().year)%100, int(datetime.today().month)%100
    elif yyear == None:
        yyear = datetime.today().year
    elif ymonth == None:
        ymonth = datetime.today().month
    main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=20%s&ymonth=%s&mzcode=K00M0409&gubun=UN'%(yyear,ymonth)

    res = requests.get(main_url,verify=False)
    soup = BeautifulSoup(res.content, 'lxml')
    date_t = []
    day_t = []
    date = soup.select('#month_iljung > dl > dd.date_info > span')
    day = soup.select('#month_iljung > dl > dd.day_info > span')

    for t in date:
        date_t.append(t.text)
    for t in day:
        day_t.append(t.text)
    
    return date_t,day_t