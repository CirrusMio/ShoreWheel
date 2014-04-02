from createDB import Person, Chore
from app import db



#adds the chore specified by the name, n, and the frequency, f.
def createChore(n, f):
  db.session.add(Chore(n, f))
  db.session.commit()

def createPerson(name, fullname):
  db.session.add(Person(name, fullname))
  db.session.commit()

def rotate():
  #TODO func rotates the weekly chores
  chores = Chore.query.filter_by(freq=1)
  people = Person.query.order_by(Person.tickets)
  people = people[::-1]
  for c in chores:
    c.assigned = people[i].displayName
    people[i].tickets += 1
    i += 1
  return

def multiSelect():
  #TODO func selects people for the multi-week chores
  return


def getPeople():
  return Person.query.order_by(Person.id)

def getChores():
  return Chore.query.order_by(Chore.id)
