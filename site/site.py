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
    temp = temperature_check()
    if temp <= 1:
        return ("Термопара не подключена")
    else:
        return (str(temp))

@app.route("/start_record", methods=['POST', 'GET'])
def start_record():
    if request.method == 'POST':
        f = open('temperature_mode.txt', 'w')
        i = 1
        for data in request.get_json():
            if i == 2:
                i = 1
                f.write(data + '\n')
            else:
                i += 1
                f.write(data + ' ')
        f.close()
    start_working()
    return render_template("graph.html")

def temperature_check():
    spi = spidev.SpiDev()
    spi.open(0,0)

    resp = spi.readbytes(2)
    temp = ((resp[1] + resp[0]*256)/8)*0.25
    return temp

def start_working():
    records = []
    with open("temperature_mode.txt", "r") as f:
        for line in f.readlines():
            records.append(line)
    while (records):
        print (records.pop(0))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True) 