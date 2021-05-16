from flask import Flask, render_template, request


app = Flask(__name__)



@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template("index.html")



@app.route("/modes", methods=['POST', 'GET'])
def modes():
    if request.method == 'POST':
        return redirect(url_for('modes'))
    return render_template("modes.html")

@app.route("/graph", methods=['POST', 'GET'])
def graph():
    if request.method == 'POST':
        return redirect(url_for('graph'))
    return render_template("graph.html")

def cur_temp():
    return "hi"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)