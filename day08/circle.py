from mymodule import Circle


# get radius from the user
while True:
        radius = float(input("Enter the radius: "))
        if radius < 0:
            print("radius cannot be negative. try again.")
        else:
            break  

# calclate and print area and circumference
r = Circle(radius)
print(f"area:{r.area()}")
print(f"circumeference: {r.circumference()}") 