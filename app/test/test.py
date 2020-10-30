import unittest
 
from app import app
 
 
class ProjectTests(unittest.TestCase):
 
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
        self.assertEquals(app.debug, False)
 
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Server - Sales Forecasting', response.data)
 
if __name__ == "__main__":
    unittest.main()