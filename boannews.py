import requests
from bs4 import BeautifulSoup

main_url = 'https://www.boannews.com/Default.asp'
res = requests.get(main_url)
soup = BeautifulSoup(res.content, 'lxml')

news_link_1 = soup.find("li",{"onmouseover":"headline_news(1);"}).get('onclick')
news_link_1 = news_link_1.replace("location.href='","")
news_link_1 = news_link_1.replace("';","")
news_link_1 = "https://www.boannews.com/"+news_link_1
news_title_1 = soup.find("li",{"onmouseover":"headline_news(1);"}).find("p").text

news_link_2 = soup.find("li",{"onmouseover":"headline_news(2);"}).get('onclick')
news_link_2 = news_link_2.replace("location.href='","")
news_link_2 = news_link_2.replace("';","")
news_link_2 = "https://www.boannews.com/"+news_link_2
news_title_2 = soup.find("li",{"onmouseover":"headline_news(2);"}).find("p").text

news_link_3 = soup.find("li",{"onmouseover":"headline_news(3);"}).get('onclick')
news_link_3 = news_link_3.replace("location.href='","")
news_link_3 = news_link_3.replace("';","")
news_link_3 = "https://www.boannews.com/"+news_link_3
news_title_3 = soup.find("li",{"onmouseover":"headline_news(3);"}).find("p").text

news_link_4 = soup.find("li",{"onmouseover":"headline_news(4);"}).get('onclick')
news_link_4 = news_link_4.replace("location.href='","")
news_link_4 = news_link_4.replace("';","")
news_link_4 = "https://www.boannews.com/"+news_link_4
news_title_4= soup.find("li",{"onmouseover":"headline_news(4);"}).find("p").text

news_link_5 = soup.find("li",{"onmouseover":"headline_news(5);"}).get('onclick')
news_link_5 = news_link_5.replace("location.href='","")
news_link_5 = news_link_5.replace("';","")
news_link_5 = "https://www.boannews.com/"+news_link_5
news_title_5 = soup.find("li",{"onmouseover":"headline_news(5);"}).find("p").text

news_img_1 = soup.find('div', id='headline0').find(class_='headline_big_img').get('style')
news_img_1 = news_img_1.replace("background: #fff url(","")
news_img_1 = news_img_1.replace(") center center no-repeat;background-size:cover;","")
news_img_1 = "https://www.boannews.com/"+news_img_1

news_img_2 = soup.find('div', id='headline0').find(class_='headline_big_img').get('style')
news_img_2 = news_img_2.replace("background: #fff url(","")
news_img_2 = news_img_2.replace(") center center no-repeat;background-size:cover;","")
news_img_2 = "https://www.boannews.com/"+news_img_2

news_img_3 = soup.find('div', id='headline0').find(class_='headline_big_img').get('style')
news_img_3 = news_img_3.replace("background: #fff url(","")
news_img_3 = news_img_3.replace(") center center no-repeat;background-size:cover;","")
news_img_3 = "https://www.boannews.com/"+news_img_3

news_img_4 = soup.find('div', id='headline0').find(class_='headline_big_img').get('style')
news_img_4 = news_img_4.replace("background: #fff url(","")
news_img_4 = news_img_4.replace(") center center no-repeat;background-size:cover;","")
news_img_4 = "https://www.boannews.com/"+news_img_4

news_img_5 = soup.find('div', id='headline0').find(class_='headline_big_img').get('style')
news_img_5 = news_img_5.replace("background: #fff url(","")
news_img_5 = news_img_5.replace(") center center no-repeat;background-size:cover;","")
news_img_5 = "https://www.boannews.com/"+news_img_5