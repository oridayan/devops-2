from flask import render_template, request, redirect, url_for
from task_calendar_app import app, db
from task_calendar_app.models import Task
import datetime

@app.route('/')
def index():
    tasks = Task.query.order_by(Task.date).all()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    title = request.form.get('title')
    date = datetime.datetime.strptime(request.form.get('date'), '%Y-%m-%d').date()
    alert = request.form.get('alert') == 'on'

    new_task = Task(title=title, date=date, alert=alert)
    db.session.add(new_task)
    db.session.commit()

    return redirect(url_for('index'))
