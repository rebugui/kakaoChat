# server.py
from flask import Flask, request, jsonify
from datetime import datetime
import sys, boannews, saramin_it, saramin_security, WS_calendar, json

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
  content = content['userRequest']
  content = content['utterance']
  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [
        {
          "simpleText": {
            "text": "test",
            "text": "test"
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
  for i in range(5):
    dataSend['template']['outputs'][0]['carousel']['items'].append(
    {
      "title": boannews.news_title_[i],
      "thumbnail": {
        "imageUrl": boannews.news_img_[i]
      },
      "buttons": [
        {
          "action": "webLink",
          "label": "구경하기",
          "webLinkUrl": boannews.news_link_[i]
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
  for i in range(3):
    dataSend['template']['outputs'][0]['carousel']['items'].append(
      {
        "header": {
          "title": "IT개발·데이터 채용 공고"
        },
        "items": []
      }       
    )
  for i in range(0,5):
      dataSend['template']['outputs'][0]['carousel']['items'][0]['items'].append(
          {
              "title": saramin_it.company_t[i],
              "description": saramin_it.title_t[i],
              "link": {
                "web": saramin_it.link_t[i]
                  }
          }
      ) 
  for i in range(5,10):
      dataSend['template']['outputs'][0]['carousel']['items'][1]['items'].append(
          {
              "title": saramin_it.company_t[i],
              "description": saramin_it.title_t[i],
              "link": {
                "web": saramin_it.link_t[i]
                  }
          }
      )
  for i in range(10,15):
      dataSend['template']['outputs'][0]['carousel']['items'][2]['items'].append(
          {
              "title": saramin_it.company_t[i],
              "description": saramin_it.title_t[i],
              "link": {
                "web": saramin_it.link_t[i]
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
  for i in range(3):
    dataSend['template']['outputs'][0]['carousel']['items'].append(
      {
        "header": {
          "title": "보안직무 채용 공고(%d)"%i
        },
        "items": []
      }       
    )
  for i in range(0,5):
    dataSend['template']['outputs'][0]['carousel']['items'][0]['items'].append(
        {
            "title": saramin_security.company_t[i],
            "description": saramin_security.title_t[i],
            "link": {
              "web": saramin_security.link_t[i]
                }
        }
    ) 
  for i in range(5,10):
      dataSend['template']['outputs'][0]['carousel']['items'][1]['items'].append(
          {
              "title": saramin_security.company_t[i],
              "description": saramin_security.title_t[i],
              "link": {
                "web": saramin_security.link_t[i]
                  }
          }
      )
  for i in range(10,15):
      dataSend['template']['outputs'][0]['carousel']['items'][2]['items'].append(
          {
              "title": saramin_security.company_t[i],
              "description": saramin_security.title_t[i],
              "link": {
                "web": saramin_security.link_t[i]
                  }
          }
      )
  return jsonify(dataSend)

@app.route('/WS_calendar', methods=['POST'])
def ws_calendar():
  ydate = request.get_json()
  ydate = json.loads(ydate['action']['detailParams']['sys_date_period']['value'])
  ydate = ydate['from']['date']
  yyear,ymonth = ydate.split('-')[0],ydate.split('-')[1]
  content = request.get_json()
  content = content['userRequest']
  content = content['utterance']
  date_t,day_t = WS_calendar.WS_calendar(yyear,ymonth)

  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [
        {
          "carousel": {
              "type": "listCard",
              "items": [
                {
                  "header": {
                    "title": "학사일정"
                  },
                  "items": []
                }
              ]
          }    
        }
      ]
    }    
  }
  if len(date_t) > 10:
    dataSend['template']['outputs'][0]['carousel']['items'].append(
      {
        "header": {
          "title": "학사일정"
        },
        "items": []
      }
    )
    dataSend['template']['outputs'][0]['carousel']['items'].append(
      {
        "header": {
          "title": "학사일정"
        },
        "items": []
      }
    )    
    for i in range(10,len(date_t)): 
      dataSend['template']['outputs'][0]['carousel']['items'][2]['items'].append(
        {
          "title": date_t[i],
          "description": day_t[i],
        }
      )
    for i in range(5,10): 
      dataSend['template']['outputs'][0]['carousel']['items'][1]['items'].append(
        {
          "title": date_t[i],
          "description": day_t[i],
        }
      )
    for i in range(0,5): 
      dataSend['template']['outputs'][0]['carousel']['items'][0]['items'].append(
        {
          "title": date_t[i],
          "description": day_t[i],
        }
      )  

  elif len(date_t) > 5:
    dataSend['template']['outputs'][0]['carousel']['items'].append(
      {
        "header": {
          "title": "학사일정"
        },
        "items": []
      }
    )    
    for i in range(0,5): 
      dataSend['template']['outputs'][0]['carousel']['items'][0]['items'].append(
        {
          "title": date_t[i],
          "description": day_t[i],
        }
      )
    for i in range(5,len(date_t)): 
      dataSend['template']['outputs'][0]['carousel']['items'][1]['items'].append(
        {
          "title": date_t[i],
          "description": day_t[i],
        }
      )
  elif len(date_t) > 0:
      for i in range(0,len(date_t)): 
        dataSend['template']['outputs'][0]['carousel']['items'][0]['items'].append(
          {
            "title": date_t[i],
            "description": day_t[i],
          }
        )
  else:
    dataSend['template']['outputs'][0]['carousel']['items'][0]['items'].append(
      {
        "title": "%s년 %s월 학사일정이 없습니다."%(yyear,ymonth)
      }
    )    
  return jsonify(dataSend)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)