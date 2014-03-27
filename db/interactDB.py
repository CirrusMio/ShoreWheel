from createDB import Person, Chore, Pair, engine

#adds the chore specified by the name, n, and the frequency, f.
def createChore(n, f):
  session = sessionmaker(bind = engine)
  session.add(Chore(name = n, freq = f))
  session.commit()

def createPerson(name, fullname):
  session = sessionmaker(bind = engine)
  session.add(Person(displayName = name, fullName = fullname, tickets = 1))
  session.commit()

def rotate():
  #TODO func rotates the weekly chores

def multiSelect():
  #TODO func selects people for the multi-week chores


def getPeople():
  session = sessionmaker(bind = engine)
  return session.query(Person).order_by(Person.id)

def getChores():
  session = sessionmaker(bind = engine)
  return session.query(Chore).order_by(Chore.id)
