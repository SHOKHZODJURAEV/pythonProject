from day03.abstraction2 import Shape, Square, Rectangle

shape1: Shape = Square(5)

shape2: Shape = Rectangle()


def display_area(shape: Shape):
    print(f'the {shape.name}\'s area is {shape.area}')

display_area(shape1)
display_area(shape2)

