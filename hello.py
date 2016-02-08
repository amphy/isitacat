import os
import json
import requests
from flask import Flask
from flask import render_template
from flask import request
#from query import Query

app = Flask(__name__)

url = "https://api.clarifai.com/v1/tag/?url="
headers = {"Authorization" : "Bearer VwtBF0lLJQ3UkGvVoyOeWCX0G4GCCa"}

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result", methods=["GET", "POST"])
def checkCat():
    img = request.form['imgurl']
    url = url + img
    r = requests.get(url, headers=headers)
    return render_template('result.html', imgurl = img)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug = True)
