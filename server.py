from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def the_home_page():
    return render_template('homepage.html')

@app.route('/roll-dice')
def dice_page():
    number = random.randint(1,6)
    return render_template('dice.html', dice_roll = number)