from flask import Flask, redirect, url_for, render_template, request
from hydro_agent import generate
import time

app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return render_template('home.html')

# Redirecting page

@app.route("/submit", methods=['POST'])
def generate_report():
    input = request.form['input']
    generate(input)   
    # time.sleep(10)
    return render_template('output.html')

@app.route("/target")
def target_page():
    return "<h1>You have been redirected to the Target Page!</h1>"

app.run(debug=True)
