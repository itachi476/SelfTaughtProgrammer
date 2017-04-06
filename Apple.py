import math


class apple:

    def __init__(self, c, w, f, t):
        self.color = c
        self.weight = w
        self.flavor = f
        self.texture = t
    print("Created!")


class circle:

    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius ** 2)


class triangle:

    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return .5 * self.base * self.height


class hexagon:

    def __init__(self, l):
        self.length = l

    def area(self):
        return self.length * 6