from app import app
from flask import Flask, render_template
from interactDB import getPeople
from seedDB import seed

@app.route('/')
def index():
  seed()
  people = getPeople()
  return render_template('template.html',people = people)

app.debug = True
app.run()
