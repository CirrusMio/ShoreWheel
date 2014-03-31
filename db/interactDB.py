from createDB import Person, Chore, Pair
from app import db



#adds the chore specified by the name, n, and the frequency, f.
def createChore(n, f):
  db.session.add(Chore(n, f))
  dbsession.commit()

def createPerson(name, fullname):
  db.session.add(Person(name, fullname))
  db.session.commit()

def rotate():
  #TODO func rotates the weekly chores
  return

def multiSelect():
  #TODO func selects people for the multi-week chores
  return


def getPeople():
  return Person.session.query.order_by(Person.id)

def getChores():
  return Chore.session.query.order_by(Chore.id)
