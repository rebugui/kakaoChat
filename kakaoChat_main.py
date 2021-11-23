# server.py
from flask import Flask, request, jsonify
import sys, boannews, saramin_it, saramin_security, WS_calendar

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
            "text": "멍청이"
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
            "items": [
              {
                "header": {
                  "title": "사람인 IT개발·데이터 채용 공고1"
                },
                "items": []
              },
              {
                "header": {
                  "title": "사람인 IT개발·데이터 채용 공고2"
                },
                "items": []
              }
            ]
          }
        }
      ]
    }
  }
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
          "listCard": {
            "header": {
              "title": "사람인 보안직무 채용 공고"
            },
            "items": [
              {
                "title": saramin_security.company_t[1],
                "description": saramin_security.title_t[1],
                "link": {
                  "web": saramin_security.link_t[1]
                }
              },
              {
                "title": saramin_security.company_t[2],
                "description": saramin_security.title_t[2],
                "link": {
                  "web": saramin_security.link_t[2]
                }
              },
              {
                "title": saramin_security.company_t[3],
                "description": saramin_security.title_t[3],
                "link": {
                  "web": saramin_security.link_t[3]
                }
              },
              {
                "title": saramin_security.company_t[4],
                "description": saramin_security.title_t[4],
                "link": {
                  "web": saramin_security.link_t[4]
                }
              },
              {
                "title": saramin_security.company_t[5],
                "description": saramin_security.title_t[5],
                "link": {
                  "web": saramin_security.link_t[5]
                }
              },
              {
                "title": saramin_security.company_t[6],
                "description": saramin_security.title_t[6],
                "link": {
                  "web": saramin_security.link_t[6]
                }
              }
            ]
          }
        }
      ]
    }
  }
  return jsonify(dataSend)

@app.route('/WS_calendar', methods=['POST'])
def ws_calendar():
  content = request.get_json()
  content = content['userRequest']
  content = content['utterance']
  dataSend = {
    "version": "2.0",
    "template": {
      "outputs": [
        {
          "listCard": {
            "header": {
              "title": "학사 일정"
            },
            "items": []
          }
        }
      ]
    }
  }
  for i in range(5): 
    dataSend['template']['outputs'][0]['listCard']['items'].append(
      {
        "title": WS_calendar.day_t[i],
        "description": WS_calendar.date_t[i],
      }
    )
  return jsonify(dataSend)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)