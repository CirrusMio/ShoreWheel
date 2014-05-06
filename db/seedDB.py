from app import db
from createDB import Person, Chore
from random import randint
from interactDB import rotate, multiSelect
from datetime import date

def createPairs():
  rotate()
  multiSelect()


def seed():
  if(len(Person.query.all())!=0):
    return
  #start the seeding
  people = [
    Person("Mike Dillon", "Mike: Original Flavor"),
    Person("Chase Southard", "Chase Original"),
    Person("Chase James", "Nu Chase"),
    Person("Tanzi Merritt", "Tanzi"),
    Person("Sarah Vessels", "Sarah"),
    Person("Todd Willey", "Todd"),
    Person("Asian Steev", "Steev"),
    Person("Will Anderson", "Will"),
    Person("Nikolai Warner", "Nick"),
    Person("Michael New-Guy", "Michael III")
  ]

  chores = [
    Chore("Load and Unload Dishwasher", 1, date.today()),
    Chore("Take Out Trash and Recycling", 1, date.today()),
    Chore("Clean Both Bathrooms", 4, date.today()),
    Chore("Mop the Floors", 4, date.today()),
    Chore("Cans to Curb and Back", 1, date.today()),
    Chore("Clean out Refridgerator", 2, date.today())
  ]

  Person.query.delete()
  Chore.query.delete()
  db.session.add_all(people)
  db.session.add_all(chores)
  db.session.commit()
  createPairs()
