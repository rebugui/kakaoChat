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
                        "carousel": {
                            "type": "card.list",
                            "cards": [
                            {
                                "listItems": [
                                  {
                                      "type": "title",
                                      "imageUrl": "https://1.bp.blogspot.com/-fHIwHKuBJCM/UfM2WqCDPqI/AAAAAAAABt0/UTK6-Ko3np4/w1200-h630-p-k-no-nu/J.Fla.jpg",
                                      "title": "Jfla",
                                      "linkUrl": {
                                        "type": "OS",
                                          "webUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "moUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "pcUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "pcCustomScheme": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "macCustomScheme": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "iosUrl": "melonios://",
                                          "iosStoreUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "androidUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "androidStoreUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264"
                                      }
                                  },
                                  {
                                      "type": "item",
                                      "imageUrl": "https://i1.sndcdn.com/artworks-000193195536-fm8ibf-t500x500.jpg",
                                      "title": "Shape of you",
                                      "description": "Ed Sheeran",
                                      "linkUrl": {
                                        "type": "OS",
                                          "webUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "moUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "pcUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "pcCustomScheme": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "macCustomScheme": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "iosUrl": "melonios://",
                                          "iosStoreUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "androidUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264",
                                          "androidStoreUrl": "http://www.melon.com/artist/timeline.htm?artistId=729264"
                                        }
                                    }
                                ]
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