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
              "items": [
                {
                  "title": boannews.news_title_[0],
                  "thumbnail": {
                    "imageUrl": boannews.news_img_[0]
                  },
                  "buttons": [
                    {
                      "action": "webLink",
                      "label": "구경하기",
                      "webLinkUrl": boannews.news_link_[0]
                    }
                  ]
                },
                {
                  "title": boannews.news_title_[1],
                  "thumbnail": {
                    "imageUrl": boannews.news_img_[1]
                  },
                  "buttons": [
                    {
                      "action": "webLink",
                      "label": "구경하기",
                      "webLinkUrl": boannews.news_link_[1]
                    }
                  ]
                },
                {
                  "title": boannews.news_title_[2],
                  "thumbnail": {
                    "imageUrl": boannews.news_img_[2]
                  },
                  "buttons": [
                    {
                      "action": "webLink",
                      "label": "구경하기",
                      "webLinkUrl": boannews.news_link_[2]
                    }
                  ]
                },
                {
                  "title": boannews.news_title_[3],
                  "thumbnail": {
                    "imageUrl": boannews.news_img_[3]
                  },
                  "buttons": [
                    {
                      "action": "webLink",
                      "label": "구경하기",
                      "webLinkUrl": boannews.news_link_[3]
                    }
                  ]
                },
                {
                  "title": boannews.news_title_[4],
                  "thumbnail": {
                    "imageUrl": boannews.news_img_[4]
                  },
                  "buttons": [
                    {
                      "action": "webLink",
                      "label": "구경하기",
                      "webLinkUrl": boannews.news_link_[4]
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