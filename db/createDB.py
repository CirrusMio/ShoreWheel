import flask from Flask
from flask.ext.sqlalchemy import SQLAlchemy

engine = create_engine('sqlite:///:memory:',echo=True)

#create a base for the tables
Base = declarative_base()

class Person(Base):
  __tablename__ = "people"

  displayName = Column(String)
  fullName = Column(String)
  tickets = Column(Integer)
  id = Column(Integer, primary_key=True)


  def __repr__(self):
    return "<Person(displayName='%s', fullName='%s', tickets='%i')>" % (self.displayName, self.fullName)

class Chore(Base):
  __tablename__ = "chores"

  name = Column(String)
  #frequency expressed in weeks
  freq = Column(Integer)
  id = Column(Integer, primary_key=True)

  def __repr__(self):
    return "<Chore(name='%s', freq='%i')>" % (self.name, self.freq)

#represents a person Chore pair
class Pair(Base):
  __tablename__ = "pairs"

  person = Column(Integer)
  chore = Column(Integer, primary_key=True)


  def __repr__(self):
    return "<Pair(chore='%i', person='%i')>" % (self.person, self.chore)

print Person.__table__
print Chore.__table__
