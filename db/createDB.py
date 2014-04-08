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
  id = db.Column(db.Integer, primary_key=True)

  def __init__(self, name, freq):
    self.name = name
    self.freq = freq
    self.assigned = ""

  def __repr__(self):
    return "<Chore(name='%s', freq='%i', assigned='%s')>" % (self.name, self.freq, self.assigned)


db.create_all()
