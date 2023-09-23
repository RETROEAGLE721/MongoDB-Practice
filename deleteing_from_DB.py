import pymongo

con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con['UserInput']
mytable = mydb['InputByUser']
print("Befor Delete")
for x in mytable.find({},{"_id":0}):
    print(x)
print("After Delete")
mytable.delete_many({})
for x in mytable.find({},{"_id":0}):
    print(x)