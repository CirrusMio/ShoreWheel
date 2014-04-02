from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('ShoreWheel')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

db = SQLAlchemy(app)
