from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
collection = database['product']
#collection.delete_one({"name": "Dell"})
result=collection.delete_many({"name": "IPhone"})
print(result.modified_count)
cursor = collection.find({"name:":"IPhone"})
for eac_doc in cursor:
    print(eac_doc)