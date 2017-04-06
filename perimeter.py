class Shape:

    def __init__(self):
        pass

    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):

    def __init__(self, l, w):
        self.length = l
        self.width = w

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Square(Shape):

    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return 4 * self.length

    def change_size(self, num):
        self.length += num


recObj = Rectangle(5, 10)
squObj = Square(7)
print((recObj.calculate_perimeter()))
print((squObj.calculate_perimeter()))
squObj.change_size(4)
print((squObj.calculate_perimeter()))
squObj.what_am_i()
