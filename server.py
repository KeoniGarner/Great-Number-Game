from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "numberGame"

@app.route('/')

def index():
    if 'number' not in session:
        session['number'] = random.randrange(0,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])

def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/playagain', methods=['POST'])

def play_again():
    session.pop('number')
    return redirect('/')

app.run(debug=True)