from collections import Counter

# list of words to count
celestial_objects = ['Moon', 'Gas', 'Asteroid', 'Dwarf', 'Asteroid', 'Moon', 'Asteroid']

# count how many times each word appear in the list
word_counts = Counter(celestial_objects)

# display the words and there counts (in the order of the list)
for word in dict.fromkeys(celestial_objects):
    print(f"{word}: {word_counts[word]}")