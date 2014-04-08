from createDB import Person, Chore
from app import db
from random import randint
from datetime import date

#adds the chore specified by the name, n, and the frequency, f.
def createChore(n, f):
  db.session.add(Chore(n, f))
  db.session.commit()

def createPerson(name, fullname):
  db.session.add(Person(name, fullname))
  db.session.commit()

def rotate():
  #TODO func rotates the weekly chores
  i = 0
  chores = Chore.query.filter_by(freq=1)

  people = Person.query.order_by(Person.tickets).all()
  people = people[::-1]
  chores = shuffle(chores.all())
  for c in chores:
    if(c.untilRotate <= 0):
<<<<<<< HEAD
=======
      c.lastRotate = date.today()
>>>>>>> 462c5fc316eaaebee86c6ccbee15d5c41b7941d5
      c.untilRotate = c.freq
      c.assigned = people[i].displayName
      people[i].tickets -= 1
      if(people[i].tickets <= 0):
        people[i].tickets = 1
      i += 1
  if(i > 0):
    for i in xrange(i,len(people)):
      people[i].tickets += 1
  db.session.commit()
  return

#shuffles an array making lottery more random
def shuffle(lst):
  result = []
  while(len(lst) != 0):
    result.append( lst.pop( randint(0, len(lst)-1) ) )
  return result


def multiSelect():
  #TODO func selects people for the multi-week chores
  totalTickets = 0
  people = Person.query.all()
  for p in people:
    totalTickets += p.tickets

  chores = Chore.query.filter(Chore.freq != 1)

  #use a modified lottery system to determine assignments
  for c in chores:
    if(c.untilRotate > 0):
      continue
    people = shuffle(people)
    lottery = randint(1,totalTickets)
    for p in people:
      lottery -= p.tickets
      if(lottery <= 0):
        if(p.tickets <= c.freq):
          totalTickets -= (p.tickets-1)
          p.tickets = 1
        else:
          totalTickets -= c.freq
          p.tickets -= c.freq

        c.assigned = p.displayName
        c.untilRotate = c.freq
        break
  db.session.commit()
  return


def getPeople():
  return Person.query.order_by(Person.id)

def getChores():
  return Chore.query.order_by(Chore.id)
