import unittest
import json

from run import app

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        # self.get_response = None


if __name__ == '__main__':
    unittest.run()