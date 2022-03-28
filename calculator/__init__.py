""" This is the Calculator Class"""
from calculator.operations import Addition, Subtraction, Multiplication, Division

class Calculator:
    """ This is the default result property"""
    result = 0

    def add(self, value_1,value_2):
        """ This is the add method"""
        self.result = value_1 + value_2
        return self.result

    def subtract(self, value_1,value_2):
        """ This is the subtract method"""
        self.result =value_1 -value_2
        return self.result


    def get_result(self):
        """ This is the get result method"""
        return self.result

    def multiply(self, value_1,value_2):
        """This is the multiply method"""
        self.result =value_1* value_2
        return  self.result

    def divide(self, value_1, value_2):
        """This is the division method"""
        try:
            self.result = value_1 /value_2
            return self.result
        except ZeroDivisionError as ex:
            raise ValueError('The second argument (value_2) must not be zero')
        except ValueError as e:
            print(e)






