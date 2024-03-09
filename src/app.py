"Importamos datetime"
from datetime import datetime
import locale
from flask import Flask, render_template

app = Flask(__name__)
locale.setlocale(locale.LC_TIME, '')



@app.route('/')
def homepage():
    "Conseguimos la hora"
    the_time = datetime.now().strftime("%A, %d %b %Y %H:%M")

    # Render HTML with variable
    return render_template("index.html", the_time=the_time, tema="cats")



@app.route('/status')
def status():
    "Devolvemos la respuesta"
    return "OK Todo"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
