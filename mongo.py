from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
print('Database created')
collection = database['product']
print('Collection Created')
product1 = [{
    "name" : "IPhone",
    "price" : 1000
    },
    {
    "name" : "Mac Book",
    "price" : 2000
    },
    {"name" : "Dell",
    "price" : 1500}]

result = collection.insert_many(product1)
print(result.inserted_ids)
