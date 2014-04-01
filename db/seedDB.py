from app import db
from createDB import Person, Chore
from random import randint

def createPairs():
  i = 0
  for c in Chore.query.all():
    if(c.freq > 1):
      c.assigned = Person.query.all()[i]
    else:
      c.assigned = Person.query.all()[i]
      i += 1
  db.session.commit()

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
  #createPairs()
