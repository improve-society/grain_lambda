import handler_lib
from pymongo import errors
import json


def categories_handler(event, context):
    try:
        resources_collection = handler_lib.get_collection('resources')
        categories_collection = handler_lib.get_collection('categories')
        json_params = json.loads(event.params)
        resources_result_set = resources_collection.find(
            {'location.map':
                 {'$within':
                      {'$center':
                           [[json_params['lat'],
                             json_params['long']],
                            json_params['radius']]
                       }
                  }
             })
        return_list = []
        for resources_result in list(resources_result_set):
            categories_result_set = categories_collection.find({'_id': {'$in': [category for category in
                                                                                resources_result['categories']]}})
            for categories_result in list(categories_result_set):
                if categories_result not in return_list:
                    return_list.append(categories_result)
        return json.dumps(return_list)

    except errors.ConnectionFailure as e:
        return 'Cannot connect to database host: %s' % e
    except errors.CollectionInvalid as e:
        return 'Invalid collection: %s' % e
    except errors.ServerSelectionTimeoutError as e:
        return 'Error: %s' % e