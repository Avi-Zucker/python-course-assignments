import sys

# make sure we got the input
if len(sys.argv) < 3:
    print("Usage: python rectangle.py <height> <width>")
    sys.exit(1)


# get height and width from the commend line
height = float(sys.argv[1])
width = float(sys.argv[2])

if height <= 0 or width <= 0:
    print("height and width must be positive numbers.")
    sys.exit(1)

# calclate and print area and perimeter
area = height*width
perimeter = 2*(height + width)
print(f"area:{area}")
print(f"perimeter: {perimeter}")