# 4.	Add a method set_marks(marks_ list), that takes a list of marks in 5 subjects and stores in a
# new attribute marks. Also add a method print_details(), to student class to print average of marks and all details of student.
# (Hint : average will be calculated as (total marks)/5 ) Test your class against the following code:
# if __name__ == ‘__main__’:
# s = Student(‘abc’, 20)
# s.set_marks([80,60,90,70,99])
# s.print_details()

def average_marks(l):
    total = 0
    for x in l:
        total += x
    ave = total / len(l)
    return ave


class Student:

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def print_details(self):
        print('Student Info: ')
        print(self._name)
        print(self._age)
        print(self._marks)
        print(average_marks(self._marks))

    def set_marks(self, l):
        self._marks = l


if __name__ == "__main__":
    s = Student('abc', 20)
    s.set_marks([80, 60, 90, 70, 99])
    s.print_details()
