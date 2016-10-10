from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps
import json


def resource_handler(event, context):
    try:
        print 'Processing: ' + context.aws_request_id
        client = MongoClient('localhost', 27017)
        db = client['grain']
        collection = db['resources']

        json_body = json.load(event.body)
        r = collection.find({'_id': json_body['_id']})
        l = list(r)

        return dumps(l)
    except errors.ConnectionFailure, e:
        #Need to pass JSONified HTTP responses back with correct Errorcodes etc.
        return "Cannot connect to database host: %s" % e
    except errors.CollectionInvalid, e:
        return "Invalid collection: %s" % e
