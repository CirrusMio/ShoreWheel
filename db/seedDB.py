from sqlalchemy import sessionmaker
from createDB import Person, Chore, Pair, engine


def createPairs():
  Session = sessionmaker(bind = engine)
  session = Session()
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
    if(len(cid) != 0):
      pairs.append(Pair(person = p, chore = cid.pop()))
    else:
      pairs.append(Pair(person = p, chore = -1))

  session.add_all(pairs)
  session.commit()

def seed():
  Session = sessionmaker(bind = engine)
  session = Session()
  #start the seeding

  people = [
    Person(displayName = 'Mike', fullName = 'Mike Dillon',tickets = 1),
    Person(displayName = 'Mike', fullName = 'Mike Dillon',tickets = 1),
    Person(displayName = 'Mike', fullName = 'Mike Dillon',tickets = 1),
    Person(displayName = 'Mike', fullName = 'Mike Dillon',tickets = 1),
    Person(displayName = 'Mike', fullName = 'Mike Dillon',tickets = 1),
    Person(displayName = 'Mike', fullName = 'Mike Dillon',tickets = 1),
    Person(displayName = 'Mike', fullName = 'Mike Dillon',tickets = 1),
    Person(displayName = 'Mike', fullName = 'Mike Dillon',tickets = 1),
  ]

  chores = [
    Chore(name = 'Dishes', freq = 1),
    Chore(name = 'Trash', freq = 1),
    Chore(name = 'Bathroom', freq = 4),
    Chore(name = 'Recycling', freq = 1),
    Chore(name = 'Stuffffff', freq = 1),
  ]

  session.add_all(people)
  session.add_all(chores)
  session.commit()
  createPairs()
