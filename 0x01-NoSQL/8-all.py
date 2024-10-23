from pymongo import MongoClient

def list_all(mongo_collection):
    client = MongoClient()
    return mongo_collection.find()
