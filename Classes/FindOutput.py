####################################
class Student:
    pass


s = Student()
s.name = "Guido"
s.age = 62
print(s.name)
print(s.age)

####################################

class Student:
    pass


s1 = Student()
s1.name = "Guido"
s1.age = 62
s2 = Student()
s2.name = 'Bjarne'
s2.age = 67
print(s1.name, s1.age)
print(s2.name, s2.age)

###################################
class Test:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")


s1 = Test()
s2 = Test()

##################################
class Test:
    def __init__(self):
        print("Constructor")

    def __del__(self):
        print("Destructor")


s1 = Test()
Test()
s2 = Test()
s3 = s1

del s1
