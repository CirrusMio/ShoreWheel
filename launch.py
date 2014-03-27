import os
import sys
sys.path.append(os.pathsep + './db/')
from flask import Flask
from interactDB import getPeople
app = Flask('ShoreWheel')

@app.route('/')
def index():
  return getPeople()


app.run()
