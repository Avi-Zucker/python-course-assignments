import sys
from rot13_module import read_file
import rot13_file

def test_main_script(tmp_path, monkeypatch):
    # Create a temporary file
    test_file = tmp_path / "test_input.txt"
    test_file.write_text("Hello World")

    # Simulate command-line arguments
    monkeypatch.setattr(sys, 'argv', ['rot13_file.py', str(test_file)])

    # Run the main function directly
    rot13_file.main()

    # Check the result
    new_content = read_file(test_file)
    assert new_content == "Uryyb Jbeyq"
