from flask import Flask, render_template, request


app = Flask(__name__)



@app.route("/", methods=['POST', 'GET'])
@app.route("/?Start=Начальная+страница ", methods=['POST', 'GET'])
def index():
     return render_template("index.html")



@app.route("/?Modes=Страница+режимов+работы ", methods=['POST', 'GET'])
def start():
     return render_template("models.html")

@app.route("/?Gaph=График+текущего+состояния ", methods=['POST', 'GET'])
def graph():
     return render_template("gaph.html")

def cur_temp():
    return "hi"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)