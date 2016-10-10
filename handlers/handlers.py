from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps
import json


def generic_handler(collection_name, context, event, ids, db_name='grain', port=27017, url='localhost'):
    try:
        print 'Processing: ' + context.aws_request_id
        client = MongoClient(url, port)
        collection = client[db_name][collection_name]
        json_body = json.load(event.body)
        result_set = collection.find({key: json_body[key] for key in ids})
        return dumps(list(result_set))
    except errors.ConnectionFailure, e:
        return "Cannot connect to database host: %s" % e
    except errors.CollectionInvalid, e:
        return "Invalid collection: %s" % e


def categories_handler(event, context):
    return generic_handler('categories', context, event, ('lat', 'long'))


def category_handler(event, context):
    return generic_handler('categories', context, event, ('_id',))


def resource_handler(event, context):
    return generic_handler('resources', context, event, ('_id',))


def resources_handler(event, context):
    return generic_handler('resources', context, event, ('_id',))
