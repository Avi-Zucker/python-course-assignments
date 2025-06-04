from collections import Counter
import sys

# make sure we got the file
if len(sys.argv) < 2:
    print("Usage: python count_digits_in_file.py <file>")
    sys.exit(1)

digit_counts = Counter({str(d): 0 for d in range(10)})

# read the file and get the digits 
filename = sys.argv[1]
with open(filename, 'r') as file:
    for line in file:
        for char in line:
            if char.isdigit():
                digit_counts[char] += 1

# write the digit counts
with open("report.txt", 'w') as report:
    for digit in map(str, range(10)):
        report.write(f"{digit} {digit_counts[digit]}\n")