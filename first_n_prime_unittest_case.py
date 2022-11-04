# import unittest package
import unittest
# import the prime_number function
from N_Prime_Number import prime_number
class TestPrime(unittest.TestCase):
    def test_three(self):
        self.assertTrue(prime_number(3))
    def test_five(self):
    	self.assertTrue(prime_number(5))
    def test_nine(self):
    	self.assertFalse(prime_number(9))
    def test_eleven(self):
    	self.assertTrue(prime_number(11))

#calling main function
if __name__=='__main__':
	unittest.main()
