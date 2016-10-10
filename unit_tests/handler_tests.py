import unittest
import handlers
import json
from mock import MagicMock


class TestHandlers(unittest.TestCase):

    def setUp(self):
        self.mock_context = MagicMock()
        self.mock_event = MagicMock()

    def tearDown(self):
        self.mock_context = None
        self.mock_event = None

    def test_categories_handler(self):
        self.mock_context.aws_request_id = 'Test1234'
        self.mock_event.body = json.dumps({'lat': '', 'long': 4})
        self.assertEqual(handlers.categories_handler())

    def test_category_handler(self):
        self.assertEqual(resources_collection.find({'name': 'Homeless Shelter'}).count(), 1)

    def test_resource_handler(self):
        self.assertEqual(ux_collection.find({'event': 'tap'}).count(), 1)

    def test_resources_handler(self):
        self.assertEqual(ux_collection.find({'event': 'tap'}).count(), 1)

if __name__ == '__main__':
    unittest.main()
