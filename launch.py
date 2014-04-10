from app import app, db
from flask import Flask, render_template, redirect, url_for
from interactDB import getPeople, getChores, rotate, multiSelect
from seedDB import seed
from datetime import timedelta, date

def update():
  chores = getChores()
  for c in chores:
    if(date.today()-c.lastRotate > timedelta(weeks=1)):
      c.untilRotate -= int((date.today()-c.lastRotate).days/7)
      c.lastRotate = date.today()
  db.session.commit()

@app.route('/')
def index():
  people = getPeople()
  chores = getChores()
  update()
  rotate()
  multiSelect()
  return render_template('template.html', people = people, chores = chores)

@app.route('/spin')
def spin():
  rotate()
  return redirect(url_for('index'))

@app.route('/multi')
def multi():
  multiSelect()
  return redirect(url_for('index'))
