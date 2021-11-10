# server.py
from flask import Flask, request, jsonify
import sys, boannews

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

@app.route('/message', methods=['POST'])
def Message():
    content = request.get_json()
    content = content['userRequest']
    content = content['utterance']

    if content == "안녕":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "",
                                    "description" : "안녕하세요"
                                }
                            ]
                        }
                    }
                ]
            }
        }

    elif content == "보안뉴스":
        dataSend = {
          "version": "2.0",
          "template": {
            "outputs": [
              {
                "listCard": {
                  "header": {
                    "title": "주요 보안뉴스스"
                  },
                  "items": [
                    {
                      "title": boannews.news_title_1,
                      "link": {
                        "web": boannews.news_link_1
                      }
                    },
                    {
                      "title": boannews.news_title_2,
                      "link": {
                        "web": boannews.news_link_2
                      }
                    },
                    {
                      "title": boannews.news_title_3,
                      "link": {
                        "web": boannews.news_link_3
                      }
                    },
                    {
                      "title": boannews.news_title_4,
                      "link": {
                        "web": boannews.news_link_4
                      }
                    },
                    {
                      "title": boannews.news_title_5,
                      "link": {
                        "web": boannews.news_link_5
                      }
                    }
                  ],
                  "buttons": [
                    {
                      "label": "보안뉴스",
                      "action": "webLink",
                      "webLinkUrl": "https://www.boannews.com/"
                    }
                  ]
                }
              }
            ]
          }
        }

    elif content == "취업정보":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "취업정보",
                                    "description" : "안녕하세요. 기능 준비중 입니다."
                                }
                            ]
                        }
                    }
                ]
            }
        }
        
        

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)                      