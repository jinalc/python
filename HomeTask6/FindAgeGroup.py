# Take input of age of 3 people by user and determine oldest and youngest among them.


def find_ageGroup(a1, a2, a3):
    res = []
    l = [a1, a2, a3]
    res.append({max(l), 'oldest'})
    res.append({min(l), 'youngest'})
    return res


a1 = int(input('Enter the age of person 1: '))
a2 = int(input('Enter the age of person 2: '))
a3 = int(input('Enter the age of person 3: '))
print(find_ageGroup(a1, a2, a3))
