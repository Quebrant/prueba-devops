from flask import Flask, render_template
from datetime import datetime
import locale

app = Flask(__name__)
locale.setlocale(locale.LC_TIME, '')


@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %D %B %Y %H:%M")

    # Render HTML with variable
    return render_template("index.html", the_time=the_time, tema="dogs")



@app.route('/status')
def status():
    return "OK Todo"


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
