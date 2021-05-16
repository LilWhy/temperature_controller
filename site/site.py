from flask import Flask, render_template, request


app = Flask(__name__)



@app.route("/", methods=['GET'])
def index():
     return render_template("index.html")

@app.route("/Start", methods=['GET'])
def index():
     return render_template("start.html")

@app.route("/Gaph", methods=['GET'])
def index():
     return render_template("gaph.html")
     
def cur_temp():
    return "hi"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)