from app import db

class Person(db.Model):
  displayName = db.Column(db.String)
  fullName = db.Column(db.String)
  tickets = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)

  def __init__(self, fullname, displayName):
    self.fullName = fullname
    self.displayName = displayName
    self.tickets = 50

  def __repr__(self):
    return "<Person(displayName='%s', fullName='%s', tickets='%i')>" % (self.displayName, self.fullName, self.tickets)

class Chore(db.Model):
  name = db.Column(db.String)
  #frequency expressed in weeks
  freq = db.Column(db.Integer)
  assigned = db.Column(db.String)
  lastRotate = db.Column(db.Date)
  untilRotate = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)

  def __init__(self, name, freq, lastRotate):
    self.name = name
    self.freq = freq
    self.untilRotate = 0
    self.assigned = ""
    self.lastRotate = lastRotate

  def __repr__(self):
    return "<Chore(name='%s', freq='%i', assigned='%s', untilRotate=%i)>" % (self.name, self.freq, self.assigned, self.untilRotate)

db.create_all()
