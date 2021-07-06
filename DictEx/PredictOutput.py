# 6. Predict Output of:

l1 = ['A', 'B', 'C', 'D', 'E']
l2 = ["Apple", " “Ball", "“Cat", "Dog", "Elephant"]
dl = dict(zip(l1, l2))

print(dl)

d2 = dict(list(dl.items())[::2])
print(d2)

# {'A': 'Apple', 'B': ' “Ball', 'C': '“Cat', 'D': 'Dog', 'E': 'Elephant'}
# {'A': 'Apple', 'C': '“Cat', 'E': 'Elephant'}