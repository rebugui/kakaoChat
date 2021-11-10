import datetime
from bs4 import BeautifulSoup as bs
import urllib.request as req

def Today_Main_Post() :
    today = datetime.datetime.today()
    today_date = today.strftime("%Y-%m\\%d.")
    today_date = str(today_date).replace("-","년").replace("\\","월").replace(".","일")
    dates= []
    titles=[]
    url = "https://www.boannews.com/media/t_list.asp"
    res = req.urlopen(url)
    soup = bs( res , "html.parser" )
    today_main_posts_title = soup.find_all("span",class_="news_txt")
    today_main_posts_dates = soup.select(" div.news_list > span.news_writer")
    tmp = today_main_posts_dates
    for ls in tmp :
        today_main_posts_dates = ls.string
        dates.append(today_main_posts_dates.split("|")[1])
    tmp = today_main_posts_title
    for ls in tmp :
        today_main_posts_title = ls.string
        titles.append(today_main_posts_title)
    i = 0
    for ls in dates :
        dates[i] = dates[i].replace(" ","")
        i += 1
    i = 0
    boolean = True
    while boolean :
        if str(dates[i][0:11]) == today_date :
            print("#%d >>"%(i+1),titles[i])
        else :
            boolean = False
        i += 1