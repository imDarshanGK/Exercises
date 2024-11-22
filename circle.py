class Circle:
    pi = 3.14
    def __init__(self, radius = 6):
        self.radius = radius
        self.area = Circle.pi * radius * radius
    def get_circumference(self):
        return 2 * Circle.pi * self.radius
circle_1 = Circle(4)
print(f"The circumference of circle 1 is: {circle_1.get_circumference()}")
circle_2 = Circle(14)
print(f"The circumference of Circle 2 is: {circle_2.get_circumference()}")
print(f"The area of circle 1 is:{ circle_1.area}")