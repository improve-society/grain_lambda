from pymongo import MongoClient
from pymongo import errors
from bson.json_util import dumps
import json


def categories_handler(event, context):
    try:
        print 'Processing: ' + context.aws_request_id
        client = MongoClient('localhost', 27017)
        db = client['grain']
        collection = db['categories']

        json_body = json.load(event.body)
        r = collection.find({'lat': json_body['lat'], 'long': json_body['long']})
        l = list(r)

        return dumps(l)
    except errors.ConnectionFailure, e:
        return "Cannot connect to database host: %s" % e
    except errors.CollectionInvalid, e:
        return "Invalid collection: %s" % e

