from flask import Flask
app = Flask(__name__)



@app.route("/")
def mainpage():
    return render_template("index.html");
def hello():
    return "Hi"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
