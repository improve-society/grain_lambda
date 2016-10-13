from pymongo import MongoClient
import json


def get_collection(collection_name, db_name='grain', port=27017, url='localhost'):
    json_cfg = read_config()
    client = MongoClient(json_cfg['url'] if json_cfg['url'] is not None else url,
                         json_cfg['port'] if json_cfg['port'] is not None else port)
    client.server_info()
    return client[db_name][collection_name]


def result_dump(result_set):
    return json.dumps(list(result_set))


def read_config():
    try:
        return json.load('../grain.cfg')
    except (OSError, IOError) as e:
        return []

