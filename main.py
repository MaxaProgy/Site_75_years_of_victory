import os
import random
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
    battles = random.sample(battles, len(battles))[:6]
    return render_template('main.html', title='Главная страница', battles=battles)


@app.route('/battle/<int:battle_id>', methods=['GET'])
def battle(battle_id):
    session = db_session.create_session()
    battle = session.query(Battle).filter(Battle.id == battle_id).first()
    return render_template('battle.html', title=battle.title, battle=battle)


@app.route('/events', methods=['GET'])
def events():
    session = db_session.create_session()
    events = session.query(Battle).all()
    return render_template('events.html', title="События", events=events)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title="О нас")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
