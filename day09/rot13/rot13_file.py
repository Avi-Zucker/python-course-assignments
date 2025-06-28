import sys
from rot13_module import read_file, write_file, rot13_transform

def main():
    if len(sys.argv) < 2:
        print("Usage: python rot13_file.py <file>")
        sys.exit(1)

    filename = sys.argv[1]

    content = read_file(filename)
    transformed = rot13_transform(content)
    write_file(filename, transformed)

if __name__ == "__main__":
    main()
