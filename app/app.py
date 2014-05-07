from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('ShoreWheel')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://shorewheel:shorewheel@localhost/shorewheel_development'

db = SQLAlchemy(app)
