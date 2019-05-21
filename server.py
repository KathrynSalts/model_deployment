from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def the_home_page():
    return 'Hello, World!'

@app.route('/ada')
def ada_page():
    return 'The ada cohort is my favorite data science cohort!'

@app.route('/roll-dice')
def dice_page():
    number = random.randint(1,6)
    return str(number)