from pymongo import MongoClient

client = MongoClient('localhost', 27017)
database = client['mydb']
print('Database created')
collection = database['product']
print('Collection Created')
product = {
    "name" : "IPhone",
    "price" : 1000
    }

result = collection.insert_one(product)
print(result.inserted_id)
