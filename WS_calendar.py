import requests, ssl
from bs4 import BeautifulSoup
from datetime import datetime
ssl._create_default_https_context = ssl._create_unverified_context

def WS_calendar(yyear,ymonth):
    if (ymonth == None) and (yyear == None):
        main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=%s&ymonth=%s&mzcode=K00M0409&gubun=UN'%(datetime.today().year,datetime.today().month)
    elif (ymonth == None) or (yyear == None):
        if yyear == None:
            main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=%s&ymonth=%s&mzcode=K00M0409&gubun=UN'%(datetime.today().year,ymonth)
        else:
            main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=%s&ymonth=%s&mzcode=K00M0409&gubun=UN'%(yyear,datetime.today().month)
    elif int(yyear)%100 == int(yyear):
        main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=20%s&ymonth=%s&mzcode=K00M0409&gubun=UN'%(yyear,ymonth)
    else:
        main_url = 'https://www.woosuk.ac.kr/classScheduleList.do?yyear=%s&ymonth=%s&mzcode=K00M0409&gubun=UN'%(yyear,ymonth)

    print(main_url)
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