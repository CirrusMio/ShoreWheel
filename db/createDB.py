from app import db

class Person(db.Model):
  displayName = db.Column(db.String)
  fullName = db.Column(db.String)
  tickets = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)

  def __init__(self, fullname, displayName):
    self.fullName = fullname
    self.displayName = displayName
    self.tickets = 1

  def __repr__(self):
    return "<Person(displayName='%s', fullName='%s', tickets='%i')>" % (self.displayName, self.fullName, self.tickets)

class Chore(db.Model):
  name = db.Column(db.String)
  #frequency expressed in weeks
  freq = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)

  def __init__(self, name, freq):
    self.name = name
    self.freq = freq

  def __repr__(self):
    return "<Chore(name='%s', freq='%i')>" % (self.name, self.freq)

#represents a person Chore pair
class Pair(db.Model):
  person = db.Column(db.Integer)
  chore = db.Column(db.Integer, primary_key=True)

  def __init__(self, person, chore):
    self.person = person
    self.chore = chore

  def __repr__(self):
    return "<Pair(chore='%i', person='%i')>" % (self.person, self.chore)

db.create_all()
