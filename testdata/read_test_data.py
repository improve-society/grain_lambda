from pymongo import MongoClient
from pymongo import errors
import unittest


class TestDatabaseInsert(unittest.TestCase):

    def test_read_categories(self):
        db = self.connect_to_database()
        categories_collection = db['categories']
        self.assertEqual(categories_collection.find({'name': 'Food Bank'}).count(), 1)

    def test_read_resources(self):
        db = self.connect_to_database()
        resources_collection = db['resources']
        self.assertEqual(resources_collection.find({'name': 'Homeless Shelter'}).count(), 1)

    def test_read_ux(self):
        db = self.connect_to_database()
        ux_collection = db['ux']
        self.assertEqual(ux_collection.find({'event': 'tap'}).count(), 1)

    def connect_to_database(self):
        try:
            client = MongoClient('localhost', 27017)
            return client['grain']
        except errors.ConnectionFailure, e:
            self.fail(e)
        except errors.CollectionInvalid, e:
            self.fail(e)

if __name__ == '__main__':
    unittest.main()
