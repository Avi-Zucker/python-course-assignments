import sys

# check that the user entered a sequence in the command line
if len(sys.argv) < 2:
    print("Usage: python dna_sequencing.py <sequens>")
    sys.exit(1)

# get the sequence from the command line
sequence = str(sys.argv[1])

# breack the sequens to parts when 'X' appear 
parts = sequence.upper().split('X')

# filter out letter 'X'
filtered = filter(None,parts)

# print the valid parts in decreasing size
print("Here are the valid parts of your sequence")
print(sorted(filtered, key = len, reverse = True))