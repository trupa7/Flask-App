import unittest
import json
import app

BASE_URL = 'http://127.0.0.1:5000/'


class MyTestCase(unittest.TestCase):
    """Test coverage for your service """
    def setUp(self):
        self.app = app.app.test_client()
        self.headers = {'Accept': 'application/json'}

    def test_get_without_accept_header(self):
        """ get response without accept header"""
        response = self.app.get(BASE_URL)
        data = response.get_data().decode('UTF-8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, '<p>Hello, World<p>')

    def test_get_with_accept_header(self):
        """ get response with  accept header"""
        response = self.app.get(BASE_URL, headers=self.headers)
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Hello, World")

    def test_get_with_accept_header_not_application_json(self):
        """ get response with  accept header but not application/json"""
        response = self.app.get(BASE_URL, headers={'Accept': 'application/javascript'})
        self.assertEqual(response.status_code, 400)

    def test_post_without_accept_header(self):
        """ post response with out accept header"""
        response = self.app.post(BASE_URL)
        data = response.get_data().decode('UTF-8')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, '<p>Hello, World<p>')

    def test_post_with_accept_header(self):
        """post response with  accept header"""
        response = self.app.post(BASE_URL, headers=self.headers)
        data = json.loads(response.get_data().decode('UTF-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], "Hello, World")

    def test_post_with_accept_header_not_application_json(self):
        """get response with  accept header  but not application/json"""
        response = self.app.post(BASE_URL, headers={'Accept': 'application/javascript'})
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
