from flask import Flask, render_template
import os


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config["DEBUG"] = True
    app.config["TESTING"] = True
    app.config["SECRET_KEY"] = os.urandom(12)
    return app

app = create_app()

@app.route('/')
def index():
    return render_template('index.html')