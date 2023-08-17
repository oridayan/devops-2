from flask import Blueprint
from flask import Flask
from flask import render_template

app = Blueprint(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')