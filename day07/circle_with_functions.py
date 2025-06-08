import math

def circle_area(radius):
   area = math.pi*radius**2
   return area
    
def circle_circumference(radius):
    circumference = math.pi*2*radius
    return circumference 

# get radius from the user
while True:
        radius = float(input("Enter the radius: "))
        if radius < 0:
            print("radius cannot be negative. try again.")
        else:
            break  

area = circle_area(radius)
print(f"area:{area}")

circumference = circle_circumference(radius)
print(f"circumeference: {circumference}")      