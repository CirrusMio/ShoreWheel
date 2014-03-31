from app import db

class Person(db.Model):
  __tablename__ = "people"

  displayName = db.Column(db.String)
  fullName = db.Column(db.String)
  tickets = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)


  def __repr__(self):
    return "<Person(displayName='%s', fullName='%s', tickets='%i')>" % (self.displayName, self.fullName)

class Chore(db.Model):
  __tablename__ = "chores"

  name = db.Column(db.String)
  #frequency expressed in weeks
  freq = db.Column(db.Integer)
  id = db.Column(db.Integer, primary_key=True)

  def __repr__(self):
    return "<Chore(name='%s', freq='%i')>" % (self.name, self.freq)

#represents a person Chore pair
class Pair(db.Model):
  __tablename__ = "pairs"

  person = db.Column(db.Integer)
  chore = db.Column(db.Integer, primary_key=True)


  def __repr__(self):
    return "<Pair(chore='%i', person='%i')>" % (self.person, self.chore)

