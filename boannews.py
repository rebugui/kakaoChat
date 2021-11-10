from urllib import request
from bs4 import BeautifulSoup

main_url = 'https://www.boannews.com/Default.asp'
res = request.get(main_url)
soup = BeautifulSoup(res.content, 'lxml')


print(soup)

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