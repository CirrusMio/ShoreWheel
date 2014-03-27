from flask import Flask
from interactDB import getPeople
from seedDB import seed
app = Flask('ShoreWheel')

@app.route('/')
def index():
  seed()
  return "Hello World"

app.debug = True
app.run()
