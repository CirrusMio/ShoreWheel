from sqlalchemy.orm import sessionmaker
from createDB import Person, Chore, Pair, engine
from random import randint

Session = sessionmaker(bind=engine)
session = Session()

def createPairs(session):
  #person ids array
  pid = []
  #chore ids array
  cid = []
  pairs = []
  for person in session.query(Person).order_by(User.id):
    pid.append(person.id)
  for chore in session.query(Chore).order_by(Chore.id):
    cid.append(chore.id)
  for p in pid:
    if(len(cid) != 0 and cid[-1].freq == 1):
      pairs.append(Pair(person = p, chore = cid.pop()))
    else:
      pairs.append(Pair(person = p, chore = -1))

  session.add_all(pairs)
  pairs = []
  people = session.query(Person).order_by(User.tickets)

  #randomly assign multi-week chores to people
  for c in session.query(Chore).order_by(Chore.freq):
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

  session.add_all(pairs)
  session.commit()

def seed():
  #start the seeding

  people = [
    Person(displayName="Mike", fullName="Mike Dillon", tickets=1),
    Person(displayName="Mike", fullName="Mike Dillon", tickets=1),
    Person(displayName="Mike", fullName="Mike Dillon", tickets=1),
    Person(displayName="Mike", fullName="Mike Dillon", tickets=1),
    Person(displayName="Mike", fullName="Mike Dillon", tickets=1),
    Person(displayName="Mike", fullName="Mike Dillon", tickets=1),
    Person(displayName="Mike", fullName="Mike Dillon", tickets=1),
    Person(displayName="Mike", fullName="Mike Dillon", tickets=1)
  ]

  chores = [
    Chore(name="Dishes", freq=1),
    Chore(name="Trash", freq=1),
    Chore(name="Bathroom", freq=4),
    Chore(name="Recycling", freq=1),
    Chore(name="Stuffffff", freq=1)
  ]

  session.add(people[0])
  #session.add(chores[0])
  session.commit()
  #createPairs(session)
  session.flush()
