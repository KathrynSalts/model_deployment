from flask import Flask, render_template
import random
import pandas as pd
from model import predict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

app = Flask(__name__)

@app.route('/')
def the_home_page():
    return render_template('homepage.html')

@app.route('/roll-dice')
def dice_page():
    number = random.randint(1,6)
    return render_template('dice.html', dice_roll = number)

@app.route('/my-first-form')
def my_first_form():
    return render_template('first_form.html')

from flask import request

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting.html', greeting=greeting)

@app.route('/model-input')
def get_model_input():
    return render_template('model_input.html')

@app.route('/model-output', methods=['POST'])
def handle_message():
    name = request.form['message']

    answer = 'This message is ' + predict(name)

    return render_template('model_output.html', answer=answer)