from app import db
from createDB import Person, Chore, Pair
from random import randint

def createPairs(session):
  #person ids array
  pid = []
  #chore ids array
  cid = []
  pairs = []
  for person in Person.query.order_by(User.id):
    pid.append(person.id)
  for chore in Chore.query.order_by(Chore.id):
    cid.append(chore.id)
  for p in pid:
    if(len(cid) != 0 and cid[-1].freq == 1):
      pairs.append(Pair(person = p, chore = cid.pop()))
    else:
      pairs.append(Pair(person = p, chore = -1))

  db.session.add_all(pairs)
  pairs = []
  people = Person.query.order_by(User.tickets)

  #randomly assign multi-week chores to people
  for c in Chore.session.query.order_by(Chore.freq):
    if(c.freq > 1):
      total = 0
      for p in people:
        total += p.tickets
      choice = randint(1,total)
      for p in people:
        total -= p.tickets
        if(total <= 0):
          pairs.append(Pair(person = p.id,chore = c.id))
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

  db.session.add(people[0])
  db.session.add(chores[1])
  db.session.commit()
