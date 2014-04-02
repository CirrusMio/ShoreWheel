from app import app
from flask import Flask, render_template
from interactDB import getPeople, getChores
from seedDB import seed

@app.route('/')
def index():
  seed()
  people = getPeople()
  chores = getChores()
  return render_template('template.html', people = people, chores = chores)

app.debug = True
app.run()
