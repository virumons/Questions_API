import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Questions_api"]
col = db["Questions"]
print(client.list_database_names())
print(db.list_collection_names())

documents = list(col.find())
print('Documents in the "questions" collection:')
for document in documents:
    print(document)

x= col.insert_one({"hello":"hell"})
print(x)
print(x.inserted_id)


