#import MongoDB to app
import pymongo
#MongoDB connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#create database
mydb = myclient["SecondeDataBase"]
#create new collection
mycol = mydb["customers"]
#create columns
mylist = [
  { "_id": 1, "name": "matin", "address": "tehran"},
  { "_id": 2, "name": "hamed", "address": "terhan"},
  { "_id": 3, "name": "ali", "address": "tehran"},
]
#insert documents
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)