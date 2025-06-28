import codecs

def read_file(filename):
    """
    Reads the content of a text file.

    Example:

    >>> with open('test_read.txt', 'w') as f:
    ...     _ = f.write('Hello World')
    
    >>> read_file('test_read.txt')
    'Hello World'
    """
    with open(filename, 'r') as file:
        return file.read()
    

def write_file(filename, content):
    """
    Writes the content to a text file.

    Example (no doctest because we can't read it back here):

    >>> write_file('test_write.txt', 'Sample content')
    """
    with open(filename, 'w') as file:
        file.write(content)



def rot13_transform(text):
    """
    Applies ROT13 cipher to the input text.

    Examples:

    >>> rot13_transform('Hello')
    'Uryyb'
    
    >>> rot13_transform('Uryyb')
    'Hello'
    
    >>> rot13_transform('Python 3.8!')
    'Clguba 3.8!'
    """
    return codecs.encode(text, 'rot_13')

if __name__ == "__main__":
    import doctest
    doctest.testmod()
