from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.delcarative import declarative_base

engine = create_engine('sqlite:///:memory:',echo=True)

#create a base for the tables
Base = declarative_base()

class Person(Base):
  __tablename__ = 'People'

  displayName = Column(String)
  fullName = Column(String)
  id = Column(Integer, primary_key=True)

  def __repr__(self):
    return "<Person(%s,%s)>" % (self.displayName, self.fullName)

class Chore(Base):
  __tablename__ = 'Chores'

  name = Column(String)
  #frequency expressed in weeks
  freq = Column(Integer)
  id = Column(Integer, primary_key=True)

  def __repr__(self):
    return "<Chore(%s,%i)>" % (self.name, self.freq)

#represents a person Chore pair
class Pair(Base):
  __tablename__ = 'Pairs'

  person = Column(Integer)
  chore = Column(Integer)

  def __repr__(self):
    return "<Pair(%i,%i)>" % (self.person, self.chore)
