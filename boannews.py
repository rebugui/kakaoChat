import requests
from bs4 import BeautifulSoup

def boannews():
 main_url = 'https://www.boannews.com/Default.asp'
 res = requests.get(main_url)
 soup = BeautifulSoup(res.content, 'lxml')
 news_title_= ["","","","",""]
 news_link_= ["","","","",""]
 news_img_= ["","","","",""]
 
 for i in range(0,5):
   news_title_[i] = soup.find("li",{"onmouseover":"headline_news(%d);"%(i+1)}).find("p").text
 
 for i in range(0,5):
   news_link_[i] = soup.find("li",{"onmouseover":"headline_news(%d);"%(i+1)}).get('onclick')
   news_link_[i] = news_link_[i].replace("location.href='","")
   news_link_[i] = news_link_[i].replace("';","")
   news_link_[i] = "https://www.boannews.com/"+news_link_[i]
 
 for i in range(0,5):
   news_img_[i] = soup.find('div', id='headline%d'%i).find(class_='headline_big_img').get('style')
   news_img_[i] = news_img_[i].replace("background: #fff url(","")
   news_img_[i] = news_img_[i].replace(") center center no-repeat;background-size:cover;","")
   news_img_[i] = "https://www.boannews.com/"+news_img_[i]
 return news_title_,news_link_,news_img_