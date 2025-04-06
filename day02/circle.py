import math

# get radius from the user
while True:
        radius = float(input("Enter the radius: "))
        if radius < 0:
            print("radius cannot be negative. try again.")
        else:
            break  

# calclate and print area and circumference
area = math.pi*radius**2
circumference = math.pi*2*radius
print(f"area:{area}")
print(f"circumeference: {circumference}")      