from mymodule import rectangle


# get height and width from the user
while True:
        height = float(input("Enter the height of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if height <= 0 or width <= 0:
            print("height and width must be positive numbers. try again.")
        else:
            break

# calclate and print area and perimeter
r = rectangle(height,width)

print(f"area:{r.area()}")
print(f"circumeference: {r.circumference()}")

