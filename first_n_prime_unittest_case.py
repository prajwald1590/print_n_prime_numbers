import unittest
# import the is_prime function
from main import prime_number
class TestPrime(unittest.TestCase):
    def test_three(self):
        self.assertTrue(prime_number(3))
    def test_five(self):
    	self.assertTrue(prime_number(5))
    def test_nine(self):
    	self.assertFalse(prime_number(9))
    def test_eleven(self):
    	self.assertTrue(prime_number(11))

if __name__=='__main__':
	unittest.main()