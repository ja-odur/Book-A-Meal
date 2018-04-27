import unittest
import json

from .run import app
from .views_v1.meals import meals_db

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        # self.get_response = None

    def tearDown(self):
        pass

    def test_create_menu(self):
        menu = [[1, 'rice and posho', 5000], [1, 'rice and posho', 5000], [1, 'rice and posho', 5000]]
        input_data = dict(menu=menu)
        expected_response_message = 'Meal {} successfully added.'.format(input_data['name'])
        get_response = self.tester.post('api/v1/menu/', content_type="application/json", data=json.dumps(input_data))

        response_results = json.loads(get_response.data.decode())
        # print(response_results)

        self.assertEqual(get_response.status_code, 201)
        self.assertEqual(expected_response_message, response_results['message'])

    # def get_menu(self):
    #     menu = [[1, 'rice and posho', 5000], [1, 'rice and posho', 5000], [1, 'rice and posho', 5000]]
    #     input_data = dict(menu=menu)
    #     expected_response_message = 'Meal {} successfully added.'.format(input_data['name'])
    #     get_response = self.tester.post('api/v1/menu/', content_type="application/json", data=json.dumps(input_data))
    #
    #     response_results = json.loads(get_response.data.decode())
    #     # print(response_results)
    #
    #     self.assertEqual(get_response.status_code, 201)
    #     self.assertEqual(expected_response_message, response_results['message'])

if __name__ == '__main__':
    unittest.main()
