import sum_of_two

from unittest import TestCase


class TestSumOfTwoNumbers(TestCase):
    """Class for testing sum of two numbers module"""


    def test_good(self):
        """Function for testing sum of two numbers module good outcome"""
        self.assertEqual(sum_of_two.sum_numbers(1,1),2)


    def test_bad(self):
        """Function for testing sum of two numbers module bad outcome"""
        self.assertNotEqual(sum_of_two.sum_numbers(1,2),2)