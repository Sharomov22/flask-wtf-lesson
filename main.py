from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/index/<page_name>')
def index(page_name):
    return render_template('base.html', title=page_name)


@app.route('/')
def default():
    return 'Миссия Колонизация Марса'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
