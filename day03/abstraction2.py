import numbers
from abc import ABC, abstractmethod

"""
abc: module name (build in module)
ABC: Abstraction class in abc module
abstractmethod: annotations that can be given to abstract methods
"""


class Volume(ABC):
    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side

    # function can not be abstract, only method can be abstract


square = Square(5)
print(square.area())


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self) -> numbers:
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def area(self) -> numbers:
        return (self.width * self.height) * self.width * self.height


class Cube(Shape, Volume):
    def area(self) -> numbers:
        pass

    def volume(self):
        pass


class Cylinder(Shape, Volume):
    def area(self) -> numbers:
        pass

    def volume(self):
        pass



