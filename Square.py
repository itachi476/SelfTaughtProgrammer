class Square:
    square_list = []

    def __init__(self, l):
        self.ln = l
        self.square_list.append(self.ln)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.ln, self.ln, self.ln, self.ln)

squObj1 = Square(8)
squObj2 = Square(7)
squObj3 = Square(1)
print((Square.square_list))
print(squObj1)