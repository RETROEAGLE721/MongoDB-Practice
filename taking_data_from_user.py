import pymongo 
con = pymongo.MongoClient("mongodb://localhost:27017")
mydb = con['UserInput']
mytable=mydb['InputByUser']
n = int(input("Enter total number of inputs:- "))
for x in range(n):
    a = input("Name: ")
    b = int(input("Age: "))
    x = mytable.insert_one({"name":a,"age":b})
for i in mytable.find({},{}).sort("age"):
    print(i)
