from flask import render_template, request, redirect, url_for
from task_calendar_app import app, db
from task_calendar_app.models import User, Task
from flask_login import login_required, current_user
import datetime

@app.route('/')
@login_required
def index():
    tasks = Task.query.order_by(Task.date).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
@login_required
def add_task():
    title = request.form.get('title')
    date = datetime.datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
    alert = request.form.get('alert') == 'on'

    new_task = Task(title=title, date=date, alert=alert)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user = User(username=username, password=password, email=email)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            return "Registration failed"
        else:
            return render_template('register.html')

    return render_template('register.html')
