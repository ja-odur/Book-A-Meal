import unittest
import json

from .api import app


class TestMeals(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        # self.get_response = None

    def test_create_meals(self):
        input_data = dict(name='meal', price=5000)
        expected_response_message = 'Meal {} successfully added.'.format(input_data['name'])
        get_response = self.tester.post('api/v1/meals/', content_type="application/json", data=json.dumps(input_data))

        # response_results = json.loads(get_response.data.decode())
        # print(response_results)

        self.assertEqual(get_response.status_code, 201)
        # self.assertEqual(expected_response_message, response_results['message'])



if __name__ == '__main__':
    unittest.main()