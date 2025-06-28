from rot13_module import rot13_transform, read_file, write_file

def test_rot13_basic():
    assert rot13_transform('Hello') == 'Uryyb'

def test_rot13_reverse():
    assert rot13_transform(rot13_transform('Hello')) == 'Hello'

def test_rot13_numbers():
    assert rot13_transform('12345') == '12345'

def test_rot13_symbols():
    assert rot13_transform('Hello!!!') == 'Uryyb!!!'

def test_read_and_write(tmp_path):
    # temp file
    test_file = tmp_path / "testfile.txt"
    write_file(test_file, 'Hello')

    # read
    content = read_file(test_file)
    assert content == 'Hello'

    # transform and write
    transformed = rot13_transform(content)
    write_file(test_file, transformed)

    new_content = read_file(test_file)
    assert new_content == 'Uryyb'
