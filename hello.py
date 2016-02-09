import os
import json
from flask import Flask
from flask import render_template
from flask import request
from clarifai2.client import ClarifaiApi

app = Flask(__name__)

clarifai_api = ClarifaiApi()
tagging = []
isCat = False

@app.route("/")
def hello():
    tagging = []
    isCat = False
    return render_template('index.html')

@app.route("/result", methods=["GET", "POST"])
def checkCat():
    tagging = []
    isCat = False
    img = request.form['imgurl']
    result = clarifai_api.tag_image_urls(img)
    res =  json.dumps(result)
    parsed_json = json.loads(res)
    imgtag = json.dumps(parsed_json['results'][0])
    parsed_json = json.loads(imgtag)
    imgtag2 = parsed_json['result']['tag']['classes']
    print imgtag2
    for x in imgtag2:
        tagging.append(x)
        print "Checking The Phrases"
        if x == "cat":
            isCat = True
    return render_template('result.html', imgurl = img, tags = tagging, isCat = isCat)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
