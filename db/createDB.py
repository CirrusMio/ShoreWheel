from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:',echo=True)

#create a base for the tables
Base = declarative_base()

class Person(Base):
  __tablename__ = "Person"

  id = Column(Integer, primary_key=True)
  displayName = Column(String)
  fullName = Column(String)
  tickets = Column(Integer)

  def __repr__(self):
    return "<Person(%s,%s)>" % (self.displayName, self.fullName)

class Chore(Base):
  __tablename__ = "Chores"

  id = Column(Integer, primary_key=True)
  name = Column(String)
  #frequency expressed in weeks
  freq = Column(Integer)

  def __repr__(self):
    return "<Chore(%s,%i)>" % (self.name, self.freq)

#represents a person Chore pair
class Pair(Base):
  __tablename__ = "Pairs"

  chore = Column(Integer, primary_key=True)
  person = Column(Integer)

  def __repr__(self):
    return "<Pair(%i,%i)>" % (self.person, self.chore)

print Person.__table__
