import os
import pytest
from ascii_art.main import read_banner, parse_banner, generate_ascii_art

# Path to the banner file for testing
TEST_BANNER_PATH = "./ascii_art/standard.txt"


def test_read_banner():
    """Test reading the banner file."""
    # Ensure the banner file exists
    assert os.path.exists(TEST_BANNER_PATH), "Banner file not found."

    # Read content from the file
    content = read_banner(TEST_BANNER_PATH)

    # Check that the content is not empty
    assert content, "Banner file is empty."


def test_parse_banner():
    """Test parsing the banner file content."""
    # Read and parse the banner file
    content = read_banner(TEST_BANNER_PATH)
    ascii_dict = parse_banner(content)

    # Ensure ASCII dictionary is populated
    assert ascii_dict, "ASCII dictionary is empty."

    # Verify that common characters are parsed correctly
    assert 'H' in ascii_dict, "'H' is missing from the ASCII dictionary."
    assert 'E' in ascii_dict, "'E' is missing from the ASCII dictionary."
    assert 'L' in ascii_dict, "'L' is missing from the ASCII dictionary."
    assert 'O' in ascii_dict, "'O' is missing from the ASCII dictionary."


def test_generate_ascii_art():
    """Test generating ASCII art for a given string."""
    # Read and parse the banner file
    content = read_banner(TEST_BANNER_PATH)
    ascii_dict = parse_banner(content)

    # Input string to convert
    string_to_convert = "{HELLO THERE}"

    # Generate ASCII art
    ascii_art = generate_ascii_art(string_to_convert, ascii_dict)

    # Ensure the output is not empty
    assert ascii_art, "Generated ASCII art is empty."

    # Debugging: Print the ASCII art to ensure correctness (can be commented out later)
    print(ascii_art)

    # Verify specific content in the generated ASCII art
    assert "  _    _   " in ascii_art, "Character 'H' is missing or incorrect in the ASCII art."
    assert "  _____   " in ascii_art, "Character 'E' is missing or incorrect in the ASCII art."
    assert " ______   _        _         ____        " in ascii_art, "Character 'O' is missing or incorrect in the ASCII art."
