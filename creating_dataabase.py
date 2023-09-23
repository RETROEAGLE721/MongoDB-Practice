import pymongo
from bson import ObjectId
# from bson.objectid import ObjectId
# print("Connecting to MongoDB....")
con = pymongo.MongoClient("mongodb://localhost:27017")
# print("connection established")
# print("Creating database...")
mydb= con['FirstDB']
# print("Database created")
# print("Cresating Coloumn.....")
mycol = mydb["FirstColumn"]
# print("Column created")
# print("Inserting data into database...")
# data = {"name":"Dhairya", "Age":"22","Gender":"Male"}
# x = mycol.insert_one(data)
# print("Data inserted successfully")
# data = {"name":"Dhairya", "Age":"22","Gender":"Male","Phome_number":"99965587.4"}
# x = mycol.insert_one(data)    
# print("Retrieving data...")
for x in mycol.find({"name":"Dhairya"},{}):
    print(x)


