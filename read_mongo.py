import pickle
from pymongo import MongoClient

def query():
    with MongoClient('mongodb://localhost:27017') as client:
        db = client.jobs
        collection = db.stock_taskmeta_collection
        for c in collection.find():
            # Fetch record from the collection
            str_result = pickle.loads(c['result'])
            str_traceback = pickle.loads(c['traceback'])
            str_children = pickle.loads(c['children'])
            print(str(str_result))
            print(str(str_traceback))
            print(str(str_children))

if __name__ == "__main__":
    query()