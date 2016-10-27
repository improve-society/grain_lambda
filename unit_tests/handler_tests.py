import unittest
from handlers import categories
from handlers import category
from handlers import resources
from handlers import resource
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
        self.mock_event.params = json.dumps({'lat': 212.5, 'long': 34234.0, 'radius': 100.0})
        result = json.loads(categories.categories_handler(self.mock_event, self.mock_context))
        self.assertEqual(len(result), 3)

    def test_category_handler(self):
        self.mock_event.params = json.dumps({'_id': 'sh1'})
        result = json.loads(category.category_handler(self.mock_event, self.mock_context))
        self.assertEqual(len(result), 1)

    def test_resource_handler(self):
        self.mock_event.params = json.dumps({'_id': 'hs1'})
        result = json.loads(resource.resource_handler(self.mock_event, self.mock_context))
        self.assertEqual(len(result), 1)

    def test_resources_handler(self):
        self.mock_event.params = json.dumps({'_id': 'sh1'})
        result = json.loads(resources.resources_handler(self.mock_event, self.mock_context))
        self.assertEqual(len(result), 2)

if __name__ == '__main__':
    unittest.main()
