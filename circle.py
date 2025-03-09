class Circle:  # Class name is Circle  
    pi = 3.14  # Class variable
    def __init__(self, radius = 6): # Constructor
        self.radius = radius    # Instance variable
        self.area = Circle.pi * radius * radius # Instance variable    
    def get_circumference(self):    # Method
        return 2 * Circle.pi * self.radius  # Method
circle_1 = Circle(20)    # Object creation
print(f"The circumference of circle 1 is: {circle_1.get_circumference()}")  # Method call
circle_2 = Circle(10)
print(f"The circumference of Circle 2 is: {circle_2.get_circumference()}")  # Method call
print(f"The area of circle 1 is:{ circle_1.area}")  # Accessing instance variable