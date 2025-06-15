import math 


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi*self.radius**2
        return area
    
    def circumference(self):
        circumference = math.pi*2*self.radius
        return circumference

class rectangle:
    def __init__(self, height,width):
        self.height = height
        self.width = width

    def area(self):
        area = self.height*self.width
        return area
    
    def circumference(self):
        circumference = 2*(self.height + self.width)
        return circumference
