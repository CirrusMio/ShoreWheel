from sqlalchemy import create_engine
from sqlalchemy.ext.delcarative import declarative_base

engine = create_engine('sqlite:///:memory:',echo=True)

#create a base for the tables
