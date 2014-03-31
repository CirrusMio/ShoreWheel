from app import app
from flask import Flask
from interactDB import getPeople
from seedDB import seed

@app.route('/')
def index():
  seed()
  return "Hello World"

app.debug = True
app.run()
