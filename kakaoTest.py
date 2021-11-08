# server.py
from flask import Flask, request, jsonify
import sys
app = Flask(__name__)


@app.route('/info')
def Keyboard():
    dataSend = {
    "Subject":"거북",
    "user":"거북"
    "이상민":"멍청이"
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

    if content == "보안뉴스":
        dataSend = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "carousel": {
                            "type" : "basicCard",
                            "items": [
                                {
                                    "title" : "보안뉴스",
                                    "description" : "안녕하세요. 기능 준비중입니다."
                                }
                            ]
                        }
                    }
                ]
            }
        }


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
    app.run(host='0.0.0.0') # Flask 기본포트 5000번
