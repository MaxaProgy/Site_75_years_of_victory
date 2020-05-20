import os

from flask import Flask, render_template
import logging


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/', methods=['GET'])
def index():
    return render_template('main.html', title='Главная страница')


if __name__ == '__main__':
    app.run()
