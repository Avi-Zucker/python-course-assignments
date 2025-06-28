import codecs
import sys

# make sure we got the file
if len(sys.argv) < 2:
    print("Usage: python rot13_file.py <file>")
    sys.exit(1)

# read the file
filename = sys.argv[1]
with open(filename, 'r') as file:

# transform the content
    content = file.read()
    transformed = codecs.encode(content, 'rot_13')

# writ the new content
with open(filename, 'w') as file:
        file.write(transformed)

