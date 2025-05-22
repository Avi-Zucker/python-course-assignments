from collections import Counter

# list of numbers to count
numbers = [1203, 1256, 312456, 98]

# we are interasted in counting digites not numbers
digit_string = ''.join(str(num) for num in numbers)

# count how many times each digit appear in the digit_string 
digit_counts = Counter(digit_string)

# display the digits and there counts (in increasing order)
for d in map(str, range(10)):
    print(f"{d}: {digit_counts.get(d, 0)}")