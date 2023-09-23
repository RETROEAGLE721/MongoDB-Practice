import pymongo 
con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con['UserInput']
myt = mydb['InputByUser']
myt.update_many({"age":43},{"$set":{"age":66}})
for x in myt.find({},{"_id":0}):
    print(x)