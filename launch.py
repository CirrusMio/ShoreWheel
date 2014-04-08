from app import app
from flask import Flask, render_template, redirect, url_for
from interactDB import getPeople, getChores, rotate, multiSelect
from seedDB import seed
from datetime import timedelta, date

def update():
  for c in getChores():
    if(c.lastRotate-date.today() > timedelta(weeks=1)):
      c.untilRotate -= int((c.lastRotate-date.today()).days/7)
      c.lastRotate = date.today()

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

if(__name__=="__main__"):
  app.debug = True
  seed()
  app.run()
