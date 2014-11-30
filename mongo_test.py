import pymongo

connection = pymongo.Connection()

db = connection["test"]
people = db["people"]

people.insert({"first":"tom","last":"jones", "age":6})

for p in db.people.find():
    print p
