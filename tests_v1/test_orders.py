import unittest
import json

from run import app

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        # self.get_response = None

    def test_create_order(self):
        order = dict(default=dict(meal=[1, 'rice and posho', 5000], caterer='default', orderId=1))

        expected_response_message = 'Menu {} successfully added.'.format(order)
        get_response = self.tester.post('api/v1/orders', content_type="application/json", data=json.dumps(order))

        response_results = json.loads(get_response.data.decode())
        # print(response_results)

        self.assertEqual(get_response.status_code, 201)
        self.assertEqual(expected_response_message, response_results['message'])

    def test_modify_order(self):
        order = dict(default=dict(meal=[1, 'rice and posho', 5000], caterer='default', orderId=1))
        modified_order = dict(default=dict(meal=[1, 'rice and posho_modified', 5000], caterer='default', orderId=1))
        expected_response_message = 'Menu {} successfully added.'.format(order)
        self.tester.post('api/v1/orders', content_type="application/json", data=json.dumps(order))
        get_response = self.tester.put('api/v1/orders/orderId', content_type="application/json", data=json.dumps(modified_order))

        response_results = json.loads(get_response.data.decode())
        # print(response_results)

        self.assertEqual(get_response.status_code, 201)
        self.assertEqual(expected_response_message, response_results['message'])

    def test_get_all_orders(self):
        expected_response_message = 'Menu {} successfully added.'.format('set value')
        get_response = self.tester.put('api/v1/orders')

        response_results = json.loads(get_response.data.decode())
        # print(response_results)

        self.assertEqual(get_response.status_code, 200)
        self.assertEqual(expected_response_message, response_results['message'])


if __name__ == '__main__':
    unittest.run()