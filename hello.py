import os
import json
from flask import Flask
from flask import render_template
from flask import request
#from query import Query
from clarifai2.client import ClarifaiApi

app = Flask(__name__)

#url = "https://api.clarifai.com/v1/tag/?url="
#headers = {"Authorization" : "Bearer VwtBF0lLJQ3UkGvVoyOeWCX0G4GCCa"}

clarifai_api = ClarifaiApi()

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result", methods=["GET", "POST"])
def checkCat():
    img = request.form['imgurl']
    result = clarifai_api.tag_image_urls(img)
    print result
    #parsed_json = json.loads(result)
    #imgtag = parsed_json['result']['tag']['classes']
    imgtag = ['cat', 'dog', 'snake']
    return render_template('result.html', imgurl = img, tags = imgtag)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug = True)
