import unittest
import json

from .apis_book_a_meal import app


class TestAPIs(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)

    # def tearDown(self):
    #     del

    def test_successful_user_registration(self):
        input_data = dict(category='user', email='default@gmail.com', username='default', password='12345',
                          confirm_password='12345', address='address1')
        expected_response_message = '{} successfully signed up.'.format(input_data['username'])
        get_response = self.tester.post('/auth/signup', content_type="application/json", data=json.dumps(input_data))

        response_results = json.loads(get_response.data.decode())
        # print(response_results)

        self.assertEqual(get_response.status_code, 201)
        self.assertEqual(expected_response_message, response_results['message'])

    def test_successful_caterer_registration(self):
        input_data = dict(category='caterer', email='default@gmail.com', username='default', password='12345',
                          confirm_password='12345', address='address1', brand_name='easy_caterer')
        expected_response_message = '{} successfully signed up.'.format(input_data['username'])
        get_response = self.tester.post('/auth/signup', content_type="application/json", data=json.dumps(input_data))

        response_results = json.loads(get_response.data.decode())

        self.assertEqual(get_response.status_code, 201)
        self.assertEqual(expected_response_message, response_results['message'])

    def test_duplicate_user_sign_up(self):
        input_data = dict(category='user', email='default@gmail.com', username='default', password='12345',
                          confirm_password='12345', address='address1')

        # initialsignup
        get_response1 = self.tester.post('/auth/signup', content_type="application/json", data=json.dumps(input_data))
        expected_response_message = '{} already exists.'.format(input_data['username'])

        #second signup
        get_response3 = self.tester.post('/auth/signup', content_type="application/json", data=json.dumps(input_data))

        response_results = json.loads(get_response3.data.decode())
        print(get_response3.status_code)
        self.assertEqual(get_response3.status_code, 401)
        self.assertEqual(expected_response_message, response_results['message'])


if __name__ == '__main__':
    unittest.main()