from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('ShoreWheel')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgesql://shorewheel:shorewheel@localhost/shorewheel_development'

db = SQLAlchemy(app)
