from unittest import TestCase
from app import app, check_currency, currency_converter

class FlaskTest(TestCase):
    def setUp(self):
            self.app = app.test_client()

    def test_main_page(self):

        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    
    def test_valid(self):
        self.assertTrue(check_currency('USD'))
        self.assertTrue(check_currency('EUR'))
        converted_amount = currency_converter.convert('USD','EUR', 100)
        self.assertIsInstance(converted_amount, (int, float))
    
    def test_invalid(self):
        self.assertFalse(check_currency('YYY'))
        self.assertFalse(check_currency('WWW'))
        
        with self.assertRaises(ValueError):
            currency_converter.convert('USD', 'YYY', 100)