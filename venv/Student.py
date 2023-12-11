class Student:
    def __init__(self, name, value):
        self.course = str(name)
        self.mark = int(value)

    def Update(self, newCourse, newMark):
            self.course = newCourse
            self.mark = newMark