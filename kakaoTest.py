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

    if content == "보안뉴스":[
        {
          "type": "card.list",
          "cards": [
            {
              "listItems": [
                {
                    "type": "title",
                    "imageUrl": "https://www.boannews.com/pds/main/default_ci.gif",
                    "title": "주요 보안뉴스",
                    "linkUrl": {
                        "type": "OS",
                        "webUrl": "https://www.boannews.com/"
                    }
                },
                {
                    "type": "item",
                    "imageUrl": "https://i1.sndcdn.com/artworks-000193195536-fm8ibf-t500x500.jpg",
                    "title": boannews.news_title_1,
                    "linkUrl": boannews.news_link_1
                }
              ]
            }
          ]
        }
    ]


    if content == "취업정보":
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