from flask import Flask, render_template, request


app = Flask(__name__)



@app.route("/", methods=['POST'])
@app.route("/index.html", methods=['POST'])
def index():
     return render_template("index.html")



@app.route("/Страница+режимов+работы", methods=['POST'])
def start():
     return render_template("models.html")

@app.route("/График+текущего+состояния", methods=['POST'])
def graph():
     return render_template("gaph.html")

def cur_temp():
    return "hi"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)