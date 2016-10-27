from pymongo import MongoClient
import json


def get_collection(collection_name, db_name='grain'):
    json_cfg = read_config()
    client = MongoClient(json_cfg['url'],
                         json_cfg['port'])
    client.server_info()
    return client[db_name][collection_name]


def result_dump(result_set):
    return json.dumps(list(result_set))


def read_config():
    try:
        return json.load('../grain.cfg')
    except AttributeError:
        return {'url': 'localhost', 'port': 27017}

