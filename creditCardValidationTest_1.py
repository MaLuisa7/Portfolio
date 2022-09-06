import unittest
from creditCardValidationTest import *

class CreditCardValidationTest(unittest.TestCase):

    def setUp(self):
        print('Setup')

    def test_validationCard_valid(self):
        result = validateCard(date(2022,12,2))
        self.assertEqual('Valid', result)

    def test_validateCard_Expired(self):
        with self.assertRaises(RuntimeError):
            validateCard(date(2020,12,2))

    def tearDown(self):
        print('TearDown')

if __name__ == '__main__':
    unittest.main()