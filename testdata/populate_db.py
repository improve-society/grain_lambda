from pymongo import MongoClient
from pymongo import errors


def populate_db():
    try:
        client = MongoClient('localhost', 27017)
        db = client['grain']
        populate_categories_collection(db)
        populate_resource_collection(db)
        populate_ux_collection(db)
    except errors.ConnectionFailure, e:
        print "Cannot connect to database host: %s" % e
    except errors.CollectionInvalid, e:
        print "Collection is invalid: %s" % e


def populate_categories_collection(db):
    categories_collection = db['categories']
    post = [{"name": "Food Bank",
             "description": "A bank for food, interest rates may vary",
             "region": "Richmond, VA"},
            {"name": "Blood Drive",
             "description": "A place to donate blood.",
             "region": "Henrico, VA"}]
    results = categories_collection.insert_many(post)
    print results.inserted_ids


def populate_resource_collection(db):
    resource_collection = db['resources']
    post = [{"name": "Homeless Shelter",
             "description": "This is a resource that provides food and shelter.",
             "categories": ["Food Bank", "Shelter"],
             "contact": {
                 "phone": "18005555555",
                 "email": "email@domain.com"
             },
             "location": {
                 "address": {
                     "street": {
                         "line1": "9313 Meadowfield Court",
                         "line2": "Apt L"
                     },
                     "city": "Glen Allen",
                     "state": "VA",
                     "zip": "23220"
                 },
                 "map": {
                     "long": 212.2345,
                     "lat": 34234
                 },
                 "region": "Richmond, VA"}
             },
            {"name": "Mobile Red Cross Van",
             "description": "This is a mobile resource that collects blood donations.",
             "categories": ["Blood Drive"],
             "contact": {
                 "phone": "18004902343",
                 "email": "email2@domain2.org"
             },
             "location": {
                 "address": {
                     "street": {
                         "line1": "4803 Bromley Lane",
                         "line2": ""
                     },
                     "city": "Richmond",
                     "state": "VA",
                     "zip": "23226"
                 },
                 "map": {
                     "long": 213.2435,
                     "lat": 34223
                 },
                 "region": "Richmond, VA"}
             }]
    results = resource_collection.insert_many(post)
    print results.inserted_ids


def populate_ux_collection(db):
    ux_collection = db['ux']
    ux_data = {"event": "tap",
               "application": {
                   "version": "2.3",
                   "id": "111111"
               },
               "device": "Xperia Zv3",
               "region": "Richmond, VA",
               "location": {
                   "X": 432.1,
                   "Y": 123.4
               }}
    result = ux_collection.insert_one(ux_data).inserted_id
    print result


populate_db()
