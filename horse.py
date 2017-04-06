class Horse:

    def __init__(self, n, o):
        self.name = n
        self.owner = o


class Rider:

    def __init__(self, n):
        self.name = n

riderObj = Rider("Randy")
horseObj = Horse("Friday", riderObj)

print((horseObj.owner.name))