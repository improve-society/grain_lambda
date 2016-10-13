from pymongo import MongoClient
import json


def get_collection(collection_name, db_name='grain', port=27017, url='localhost'):
    client = MongoClient(url, port)
    client.server_info()
    return client[db_name][collection_name]


def result_dump(result_set):
    return json.dumps(list(result_set))

