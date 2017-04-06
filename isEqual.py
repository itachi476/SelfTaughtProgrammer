class Student:

    def __init__(self):
        pass


class Teacher:

    def __init__(self):
        pass

Cameron = Student()
Berrett = Teacher()
Kevin = Student()


def isEqual(Obj1, Obj2):
    print((Obj1 is Obj2))

isEqual(Cameron, Berrett)
isEqual(Cameron, Kevin)
isEqual(Kevin, Berrett)

Cameron = Kevin

isEqual(Cameron, Kevin)