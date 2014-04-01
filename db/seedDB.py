from app import db
from createDB import Person, Chore, Pair
from random import randint

def createPairs():
  #person ids array
  pid = []
  #chore ids array
  cid = []
  pairs = []
  for person in Person.query.order_by(Person.id):
    pid.append(person.id)
  for chore in Chore.query.order_by(Chore.id):
    cid.append(chore.id)
  chores = Chore.query.order_by(Chore.id)
  for p in pid:
    if(len(cid) != 0 and chores[-1].freq == 1):
      pairs.append(Pair(p, cid.pop()))
    else:
      pairs.append(Pair(p,-1))

  db.session.add_all(pairs)
  pairs = []
  people = Person.query.order_by(Person.tickets)

  #randomly assign multi-week chores to people
  for c in Chore.query.order_by(Chore.freq):
    if(c.freq > 1):
      total = 0
      for p in people:
        total += p.tickets
      choice = randint(1,total)
      for p in people:
        total -= p.tickets
        if(total <= 0):
          pairs.append(Pair(p.id,c.id))
          p.tickets -= c.freq

  db.session.add_all(pairs)
  db.session.commit()

def seed():
  #start the seeding

  people = [
    Person("Mike", "Mike Dillon"),
    Person("Mike", "Mike Dillon"),
    Person("Mike", "Mike Dillon"),
    Person("Mike", "Mike Dillon"),
    Person("Mike", "Mike Dillon"),
    Person("Mike", "Mike Dillon"),
    Person("Mike", "Mike Dillon"),
    Person("Mike", "Mike Dillon")
  ]

  chores = [
    Chore("Dishes", 1),
    Chore("Trash", 1),
    Chore("Bathroom", 4),
    Chore("Recycling", 1),
    Chore("Stuffffff", 1)
  ]
  Person.query.delete()
  Chore.query.delete()
  Pair.query.delete()
  db.session.add_all(people)
  db.session.add_all(chores)
  db.session.commit()
  createPairs()
