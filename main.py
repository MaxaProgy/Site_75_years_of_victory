import os

from flask import Flask, render_template
import logging

from data import db_session
from data.battle import Battle
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
db_session.global_init("db/battle.sqlite")


@app.route('/', methods=['GET'])
def index():
    session = db_session.create_session()
    battles = session.query(Battle).all()
    return render_template('main.html', title='Главная страница', battles=battles)


if __name__ == '__main__':
    app.run()
