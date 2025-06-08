from collections import Counter
import sys
import re

# make sure we got the file
if len(sys.argv) < 2:
    print("Usage: python count_words_from_a_file.py <file>")
    sys.exit(1)

# read the file and count words 
filename = sys.argv[1]
with open(filename, 'r') as file:
    words = re.findall(r'\b\w+\b', file.read().lower())
    word_counts = Counter(words)


# write the word counts
with open("report.txt", 'w') as report:
    for word in sorted(word_counts):
        report.write(f"{word} {word_counts[word]}\n")