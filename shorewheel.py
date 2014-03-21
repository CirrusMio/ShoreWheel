import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  url_for('static',filename='frontend.html')
