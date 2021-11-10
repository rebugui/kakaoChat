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
                  "simpleText": {
                    "text": "간단한 텍스트 요소입니다."
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
                "carousel": {
                  "type": "basicCard",
                  "items": [
                    {
                      "title": boannews.news_title_1,
                      "thumbnail": {
                        "imageUrl": boannews.news_img_1
                      },
                      "buttons": [
                        {
                          "action": "webLink",
                          "label": "구경하기",
                          "webLinkUrl": boannews.news_link_1
                        }
                      ]
                    },
                    {
                      "title": boannews.news_title_2,
                      "thumbnail": {
                        "imageUrl": boannews.news_img_2
                      },
                      "buttons": [
                        {
                          "action": "webLink",
                          "label": "구경하기",
                          "webLinkUrl": boannews.news_link_2
                        }
                      ]
                    },
                    {
                      "title": boannews.news_title_3,
                      "thumbnail": {
                        "imageUrl": boannews.news_img_3
                      },
                      "buttons": [
                        {
                          "action": "webLink",
                          "label": "구경하기",
                          "webLinkUrl": boannews.news_link_3
                        }
                      ]
                    },
                    {
                      "title": boannews.news_title_4,
                      "thumbnail": {
                        "imageUrl": boannews.news_img_4
                      },
                      "buttons": [
                        {
                          "action": "webLink",
                          "label": "구경하기",
                          "webLinkUrl": boannews.news_link_4
                        }
                      ]
                    },
                    {
                      "title": boannews.news_title_5,
                      "thumbnail": {
                        "imageUrl": boannews.news_img_5
                      },
                      "buttons": [
                        {
                          "action": "webLink",
                          "label": "구경하기",
                          "webLinkUrl": boannews.news_title_5
                        }
                      ]
                    },
                  ]
                }
              }
            ]
          }
          
        }

    return jsonify(dataSend)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)                      