import math
import sys

# make sure we got the input
if len(sys.argv) < 2:
    print("Usage: python circle.py <radius>")
    sys.exit(1)


# get radius from the commend line
radius = float(sys.argv[1])
if radius < 0:
    print("radius cannot be negative.")
    sys.exit(1)
    
# calclate and print area and circumference
area = math.pi*radius**2
circumference = math.pi*2*radius
print(f"area:{area}")
print(f"circumeference: {circumference}")      