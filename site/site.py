from flask import Flask, request, url_for, redirect, render_template
import spidev
import time


app = Flask(__name__)



@app.route("/index", methods=['POST', 'GET'])
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

@app.route("/temperature", methods=['POST', 'GET'])
def temperature():
    spi = spidev.SpiDev()
    spi.open(0,0)

    resp = spi.readbytes(2)
    temp = ((resp[1] + resp[0]*256)/8)*0.25
    if temp <= 1:
        return ("Термопара не подключена")
    else:
        return (str(temp))

@app.route("/start_record", methods=['POST', 'GET'])
def start_record():
    if request.method == 'POST':
        print(request.get_json()[0])
    return render_template("graph.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)