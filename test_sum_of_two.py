''' Unittest of sum of two'''

import sum_of_two

def test_good():
    """Function for testing sum of two numbers module good outcome"""
    assert sum_of_two.sum_numbers(1,1) == 2


def test_bad():
    """Function for testing sum of two numbers module bad outcome"""
    assert sum_of_two.sum_numbers(1,2) != 2
