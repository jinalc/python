# 5. Create a class Circle, that stores the radius and contains 2 methods:
# get_area, get_perimeter, which give the area and perimeter respectively of the circle.

class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        return 3.14 * self._radius * self._radius

    def get_perimeter(self):
        return 2 * 3.14 * self._radius


if __name__ == "__main__":
    c = Circle(10)
    print(c.get_area())
    print(c.get_perimeter())
