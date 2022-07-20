# -*- coding: utf-8 -*-

import os
import random
from flask import Flask, render_template
import logging

logging.basicConfig(level=logging.INFO)
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/battle.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['FLASK_ADMIN_SWATCH'] = 'cosmo'
app.config['BABEL_DEFAULT_LOCATE'] = 'ru'

db = SQLAlchemy(app)


@app.route('/', methods=['GET'])
def index():
    from data.battle import Battle
    battles = Battle.query.all()
    battles = random.sample(battles, len(battles))[:6]
    return render_template('main.html', title='Главная страница', battles=battles)


@app.route('/battle/<int:battle_id>', methods=['GET'])
def battle(battle_id):
    from data.battle import Battle
    battle = Battle.query.filter(Battle.id == battle_id).first()
    return render_template('battle.html', title=battle.title, battle=battle)


@app.route('/events', methods=['GET'])
def events():
    from data.battle import Battle
    events = Battle.query.all()
    return render_template('events.html', title="События", events=events)


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html', title="О нас")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
