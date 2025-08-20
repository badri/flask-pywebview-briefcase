import unittest
from flask_pywebview_app.app import create_app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
    
    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_hello_api(self):
        response = self.client.get('/api/hello')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('message', data)
        self.assertEqual(data['message'], 'Hello from Flask!')
    
    def test_info_api(self):
        response = self.client.get('/api/info')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn('app_name', data)
        self.assertEqual(data['app_name'], 'Flask PyWebView App')

if __name__ == '__main__':
    unittest.main()
