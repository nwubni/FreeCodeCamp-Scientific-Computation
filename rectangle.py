class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if(self.width > 50 or self.height > 50):
            return "Too big for picture."

        shape = ''

        for i in range(0, self.height):
            shape += '*' * self.width + '\n'

        return shape

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __repr__(self):
        return '{class_name}(width={width}, height={height})'.format(class_name=self.__class__.__name__, width=self.width, height=self.height)


class Square(Rectangle):
    def __init__(self, side):
        Rectangle.__init__(self, side, side)

    def set_side(self, side):
        Rectangle.set_height(self, side)
        Rectangle.set_width(self, side)

    def __repr__(self):
        return '{class_name}(side={side})'.format(class_name=self.__class__.__name__, side=Rectangle.get_width(self))


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())


sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
