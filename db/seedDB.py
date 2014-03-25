from sqlalchemy import sessionmaker
import createDB


def seed():
  Session = sessionmaker(bind = engine)
  session = Session()
  #start the seeding

  people = [
    Person(displayName = 'Mike', fullName = 'Mike Dillon'),
    Person(displayName = 'Mike', fullName = 'Mike Dillon'),
    Person(displayName = 'Mike', fullName = 'Mike Dillon'),
    Person(displayName = 'Mike', fullName = 'Mike Dillon'),
    Person(displayName = 'Mike', fullName = 'Mike Dillon'),
    Person(displayName = 'Mike', fullName = 'Mike Dillon'),
    Person(displayName = 'Mike', fullName = 'Mike Dillon'),
    Person(displayName = 'Mike', fullName = 'Mike Dillon'),
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
