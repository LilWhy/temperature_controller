from flask import Flask
app = Flask(__name__)



@app.route("/")
def mainpage():
    return: '''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Нижний индекс</title>
 </head>
 <body>
  <p><b>Формула серной кислоты:</b> <i>H<sub>2</sub>SO<sub>4</sub></i></p>
 </body>
</html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
