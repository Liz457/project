""" These are the Operation Classes"""


class Addition:
    """This is the addition class"""

    # this defines a static method that you can use without instantiating the class
    @staticmethod
    def add(value_1, value_2):
        """ This is the add method"""
        return value_1 + value_2


class Subtraction:
    """This is the subtraction class"""

    @staticmethod
    def subtract(value_1, value_2):
        """This is the subtract method"""
        return value_1 - value_2

class Multiplication:
    """This is the multiplication method"""

    @staticmethod
    def multiply(value_1, value_2):
        """This is the add method"""
        return value_1 * value_2

class Division:
    """This is the division method"""
    
    @staticmethod
    def divide(value_1, value_2):
        """This is the division method"""
        return value_1 / value_2
