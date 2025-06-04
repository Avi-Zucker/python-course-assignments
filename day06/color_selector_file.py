import sys

# make sure we got the file
if len(sys.argv) < 2:
    print("Usage: python color_selector_file.py <file>")
    sys.exit(1)

# read the file
filename = sys.argv[1]
with open(filename, 'r') as file:

# list the lines and print them in a Numbered list
    lines = [line.rstrip('\n') for line in file]
    for i, line in enumerate(lines, start=1):
        print(f"{i}. {line}")

# get the user choice 
color = int(input("Please pick a number from the list: "))

# if the choice is valide print the color
if 1 <= color <= len(lines):
     selected = lines[color - 1]
     print("You selected: ", selected)
else:
     print("Invalid choice: number out of range")
