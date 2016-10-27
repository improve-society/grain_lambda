import handler_lib
from pymongo import errors
import json


def resources_handler(event, context):
    try:
        collection = handler_lib.get_collection('resources')
        json_params = json.loads(event.params)
        return handler_lib.result_dump(collection.find({'categories' : json_params['_id']}))
    except errors.ConnectionFailure as e:
        return 'Cannot connect to database host: %s' % e
    except errors.CollectionInvalid as e:
        return 'Invalid collection: %s' % e
    except errors.ServerSelectionTimeoutError as e:
        return 'Error: %s' % e
