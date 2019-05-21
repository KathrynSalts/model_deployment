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