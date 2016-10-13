import handler_lib
from pymongo import errors
import json


def categories_handler(event, context):
    try:
        resources_collection = handler_lib.get_collection('resources')
        categories_collection = handler_lib.get_collection('categories')
        json_body = json.loads(event.body)
        print json_body
        test = [json_body['lat'], json_body['long']]
        print test
        resources_result_set = resources_collection.find(
            {'map': test})
            # {'map':
            #      {'$within':
            #           {'$center':
            #                [[json_body['lat'],
            #                  json_body['long']],
            #                 json_body['radius']]
            #            }
            #       }
            #  })
        print list(resources_result_set)
        return_list = []
        for resources_result in resources_result_set:
            categories_result_set = categories_collection.find({'_id': {'$in': [category for category in
                                                                                list(resources_result)['categories']]}})
            for categories_result in categories_result_set:
                return_list.append(list(categories_result))
        return json.dumps(return_list)

    except errors.ConnectionFailure as e:
        return 'Cannot connect to database host: %s' % e
    except errors.CollectionInvalid as e:
        return 'Invalid collection: %s' % e
    except errors.ServerSelectionTimeoutError as e:
        return 'Error: %s' % e