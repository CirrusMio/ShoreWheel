from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('ShoreWheel')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

db = SQLAlchemy(app)
