from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
collection = database['product']
#print(collection.find_one())
cursor = collection.find({"name:":"Dell"})
for eac_doc in cursor:
    print(eac_doc)
