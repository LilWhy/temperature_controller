from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
           return render_template("index.html")

        elif  request.form.get('Gaph') == 'Gaph':
            return render_template("gaph.html")

        elif  request.form.get('Modes') == 'Modes':
            return render_template("modes.html")
        else:
                # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
            # return render_template("index.html")
        print("No Post Back Call")
    return render_template("index.html")

def cur_temp():
    return "hi"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)