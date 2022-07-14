class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    # overload less than
    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag


class Parent:  # define parent class
    def __init__(self, prop1=0, prop2="some text"):
        self.prop1 = prop1
        self.prop2 = prop2

    @staticmethod
    def myMethod():
        return 'Calling parent method'

    @staticmethod
    def addition_number_method(a, b):
        return a + b


class Child(Parent):  # define child class
    """
    """
    @staticmethod
    def myMethod():
        return 'Calling child method'
