import os
from flask import Flask,url_for,redirect

app = Flask(__name__,static_url_path='')

@app.route('/')
def hello():
  return redirect(url_for('static',filename='frontend.html'))
