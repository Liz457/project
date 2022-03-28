""" This is the Calculator Class"""


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
        self.result = value_1 /value_2
        return self.result

