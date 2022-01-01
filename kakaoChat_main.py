# -*- coding: utf-8 -*-
# server.py
from flask import Flask, request, jsonify
from datetime import datetime
import sys, boannews, saramin, WS_calendar, json

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'


@app.route('/info')
def Keyboard():
  dataSend = {
  "Subject":"거북",
  "user":"거북"
  }
  return jsonify(dataSend)

@app.route('/test', methods=['POST'])
def test():
  content = request.get_json()
  print("입력 테스트 입니다.")
  print(content)
  content = content['userRequest']
  content = content['utterance']
  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [{
        "simpleText": {
          "text": "간단한 텍스트 요소입니다."
          }
        }
      ]
    }
  }
  return jsonify(dataSend)

@app.route('/KrCheck_result', methods=['POST'])
def KrCheck_result():
  content = request.get_json()
  content = content['userRequest']
  content = content['utterance']
  input_text = request.get_json()
  input_text = json.loads(input_text['action']['detailParams'])
  print (input_text)

  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [{
        "simpleText": {
          "text": "입력 값입니다.: %s"%(input_text)
          }
        }
      ]
    }
  }
  return jsonify(dataSend)

@app.route('/boannews_print', methods=['POST'])
def boannews_print():
  content = request.get_json()
  content = content['userRequest']
  content = content['utterance']
  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [
        {
          "carousel": {
            "type": "basicCard",
            "items": []
          }
        }
      ]
    }
  }
  news_title_,news_link_,news_img_ = boannews.boannews()
  for i in range(5):
    dataSend['template']['outputs'][0]['carousel']['items'].append(
    {
      "title": news_title_[i],
      "thumbnail": {
        "imageUrl": news_img_[i]
      },
      "buttons": [
        {
          "action": "webLink",
          "label": "구경하기",
          "webLinkUrl": news_link_[i]
        }
      ]
    })
  return jsonify(dataSend)

@app.route('/saramin_it_list', methods=['POST'])
def saramin_it_list():
  content = request.get_json()
  content = content['userRequest']
  content = content['utterance']
  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [
        {
          "carousel": {
            "type": "listCard",
            "items": []
          }
        }
      ]
    }
  }
  company_t,title_t,link_t = saramin.it()

  for i in range(3):
    dataSend['template']['outputs'][0]['carousel']['items'].append(
      {
        "header": {
          "title": "IT개발·데이터 채용 공고"
        },
        "items": []
      }       
    )
    for t in range(5):
      t = t + (i * 5)
          
      dataSend['template']['outputs'][0]['carousel']['items'][i]['items'].append(
        {
          "title": company_t[t],
          "description": title_t[t],
          "link": {
            "web": link_t[t]
              }
        }
      )
  return jsonify(dataSend)

@app.route('/saramin_security_list', methods=['POST'])
def saramin_security_list():
  content = request.get_json()
  content = content['userRequest']
  content = content['utterance']
  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [
        {
          "carousel": {
            "type": "listCard",
            "items": []
          }
        }
      ]
    }
  }
  company_t,title_t,link_t = saramin.security()
  for i in range(3):
    dataSend['template']['outputs'][0]['carousel']['items'].append(
      {
        "header": {
          "title": "보안직무 채용 공고"
        },
        "items": []
      }       
    )
    for t in range(5):
      t = t + (i * 5)
      dataSend['template']['outputs'][0]['carousel']['items'][i]['items'].append(
        {
          "title": company_t[t],
          "description": title_t[t],
          "link": {
            "web": link_t[t]
              }
        }
      )
  return jsonify(dataSend)

@app.route('/WS_calendar', methods=['POST'])
def ws_calendar():
  content = request.get_json()
  content = content['userRequest']
  content = content['utterance']
  ydate = request.get_json()
  ydate = json.loads(ydate['action']['detailParams']['sys_date_period']['value'])
  ydate = ydate['from']['date']
  yyear,ymonth = int(ydate.split('-')[0])%100,ydate.split('-')[1]
  date_t,day_t = WS_calendar.WS_calendar(yyear,ymonth)
  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [
        {
          "carousel": {
              "type": "listCard",
              "items": []
          }    
        }
      ]
    }    
  }
  item_count = (len(date_t) // 5)
  if (len(date_t) % 5) > 0:
    item_count = item_count + 1

  if len(date_t) == 0:
    dataSend['template']['outputs'][0]['carousel']['items'].append(
        {
          "header": {
            "title": "학사일정"
          },
          "items": [
            {
              "title": "20%s년 %s월 학사일정이 없습니다."%(yyear,ymonth),
            }
          ]
        }
      )    
  else:
    for i in range(item_count):
      dataSend['template']['outputs'][0]['carousel']['items'].append(
        {
          "header": {
            "title": "학사일정"
          },
          "items": []
        }
      )
      for t in range(5):
        t = t + (i * 5)
        if t >= len(date_t):
          break
        dataSend['template']['outputs'][0]['carousel']['items'][i]['items'].append(
          {
            "title": date_t[t],
            "description": day_t[t]
          }
        )
  return jsonify(dataSend)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)