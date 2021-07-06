# 2.	For the Student class in above example, add constructor with 2 arguments for name and age, to set the name and age attributes. Create a student object,
# initialize it with some values and print its attributes.


class Student:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def printStudent(self):
        print(self._name)
        print(self._age)


s1 = Student("Jinal", 27)
s1.printStudent()
