from app import db
from createDB import Person, Chore
from random import randint

def createPairs():
  i = 0
  chores = Chore.query.all()
  people = Person.query.all()
  for c in chores:
    if(c.freq > 1):
      c.assigned = people[i].displayName
      people[i].tickets += 1
    else:
      c.assigned = people[i].displayName
      people[i].tickets += 1
      i += 1


def seed():
  #start the seeding

  people = [
    Person("Mike", "Mike Dillon"),
    Person("Chase Original", "Original Chase"),
    Person("Nu Chase", "New Chase"),
    Person("Tanzi", "Tanzi Merritt"),
    Person("Sarah", "Sarah Vessels"),
    Person("Todd", "Todd Willey"),
    Person("Steev", "Asian Steev"),
    Person("Will", "Asian Will")
  ]

  chores = [
    Chore("Dishes", 1),
    Chore("Trash", 1),
    Chore("Bathroom", 4),
    Chore("Pay Interns", 4),
    Chore("Recycling", 1),
    Chore("Stuffffff", 1)
  ]
  Person.query.delete()
  Chore.query.delete()
  db.session.add_all(people)
  db.session.add_all(chores)
  db.session.commit()
  createPairs()
