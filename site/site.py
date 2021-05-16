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

@app.route("/graph", methods=['POST', 'GET']
def cur_temp():
    spi = spidev.SpiDev()
    spi.open(0,0)

    resp = spi.readbytes(2)
    temp = ((resp[1] + resp[0]*256)/8)*0.25
    time.sleep(1)
    temp += ((resp[1] + resp[0]*256)/8)*0.25
    time.sleep(1)
    temp += ((resp[1] + resp[0]*256)/8)*0.25
    temp = temp // 3
    return (temp)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)