import re

# get a sequence from the user
sequence = str(input("Please type in a sequence: "))

# breack the sequens to parts when non-valid letter appear 
parts = re.split(r'[^ACTG]', sequence.upper())

# filter out the non-valid letter
filtered = filter(None,parts)

# print the valid parts in decreasing size
print("Here are the valid parts of your sequence")
print(sorted(filtered, key = len, reverse = True))