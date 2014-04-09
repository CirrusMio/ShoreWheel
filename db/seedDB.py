from app import db
from createDB import Person, Chore
from random import randint
from interactDB import rotate, multiSelect
from datetime import date

def createPairs():
  rotate()
  multiSelect()


def seed():
  #start the seeding
  people = [
    Person("Mike Dillon", "Mike"),
    Person("Original Chase", "Chase Original"),
    Person("New Chase", "Nu Chase"),
    Person("Tanzi Merritt", "Tanzi"),
    Person("Sarah Vessels", "Sarah"),
    Person("Todd Willey", "Todd"),
    Person("Asian Steev", "Steev"),
    Person("Asian Will", "Will")
  ]

  chores = [
    Chore("Dishes", 1, date.today()),
    Chore("Trash", 1, date.today()),
    Chore("Bathroom", 4, date.today()),
    Chore("Pay Interns", 4, date.today()),
    Chore("Recycling", 1, date.today()),
    Chore("Stuffffff", 1, date.today())
  ]

  Person.query.delete()
  Chore.query.delete()
  db.session.add_all(people)
  db.session.add_all(chores)
  db.session.commit()
  createPairs()
