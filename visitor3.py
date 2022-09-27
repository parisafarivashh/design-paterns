
class CourseOnline:

    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, 'thought by', visitor, visitor.name)

    def studing(self, visitor):
        print(self, 'studing by', visitor, visitor.name)

    def __str__(self):
        return self.__class__.__name__


class English(CourseOnline):
    pass


class French(CourseOnline):
    pass


class Visitor:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.__class__.__name__


class Teacher(Visitor):
    def visit(self, corseclass):
        corseclass.teaching(self)


class Student(Visitor):
    def visit(self, corseclass):
        corseclass.studing(self)


english = English()
french = French()

teacher = Teacher(name='sara')
student = Student(name='saman')

english.accept(teacher)
english.accept(student)

french.accept(teacher)
french.accept(student)

