
import logging

from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

app = Flask(__name__)

ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('BeginIntent')
def begin():
    miku_song = render_template('play')
    return statement(miku_song)


@ask.intent('AMAZON.StopIntent')
def stop():
    text = render_template('stop')
    return statement(bye_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    bye_text = render_template('bye')
    return statement(bye_text)


@ask.session_ended
def session_ended():
    return "", 200


if __name__ == '__main__':

    app.run(debug=True)
