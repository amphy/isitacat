import os
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/result", methods=["GET", "POST"])
def checkCat():
    img = request.form['imgurl']
    #print img
    return render_template('result.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run(debug = True)
