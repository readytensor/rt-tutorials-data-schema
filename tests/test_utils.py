"""
This module contains unit tests for the `read_json_as_dict` function of the utils.py module.

`read_json_as_dict` is a utility function that reads a JSON file and returns its content as a dictionary.
It can handle both direct file paths and directories containing a JSON file.
If the provided path is neither a file nor a directory, the function raises a ValueError.

The tests included in this module verify the correct functionality of `read_json_as_dict` for various
scenarios, including:
- When a direct path to a JSON file is provided.
- When a path to a directory containing a JSON file is provided.
- When an invalid path is provided.
- When there is no JSON file in the given directory.
- When the JSON file is invalid.
"""

import json
import os
import shutil
import tempfile
import pytest

from src.utils import read_json_as_dict


def test_read_json_as_dict_with_file_path():
    """
    Test if `read_json_as_dict` function can correctly read a JSON file
    and return its content as a dictionary when given a file path.
    """
    # Given
    input_dict = {"key": "value"}
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, "test.json")
    
    with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        json.dump(input_dict, temp_file)

    # When
    result_dict = read_json_as_dict(temp_file_path)

    # Then
    assert result_dict == input_dict

    # Cleanup
    shutil.rmtree(temp_dir)


def test_read_json_as_dict_with_dir_path():
    """
    Test if `read_json_as_dict` function can correctly find a JSON file in a directory,
    read the file, and return its content as a dictionary when given a directory path.
    """
    # Given
    input_dict = {"key": "value"}
    temp_dir = tempfile.mkdtemp()
    temp_file_path = os.path.join(temp_dir, "test.json")
    
    with open(temp_file_path, 'w', encoding='utf-8') as temp_file:
        json.dump(input_dict, temp_file)

    # When
    result_dict = read_json_as_dict(temp_dir)

    # Then
    assert result_dict == input_dict

    # Cleanup
    shutil.rmtree(temp_dir)


def test_read_json_as_dict_with_invalid_path():
    """
    Test if `read_json_as_dict` function correctly raises a ValueError when given an invalid path.
    """
    # Given
    invalid_path = "/invalid/path"

    # When/Then
    with pytest.raises(ValueError):
        read_json_as_dict(invalid_path)


def test_read_json_as_dict_no_json_file(tmpdir):
    """
    Test the read_json_as_dict function for a directory that does not contain any JSON file.
    The function should raise an exception.
    """
    # Given: A temporary directory without any JSON file
    directory_path = tmpdir.mkdir("subdir")
    
    # When: read_json_as_dict is called with the directory path
    # Then: A ValueError should be raised
    with pytest.raises(ValueError):
        read_json_as_dict(directory_path)


def test_read_json_as_dict_invalid_json_file(tmpdir):
    """
    Test the read_json_as_dict function with an invalid JSON file.
    """
    # Given: Create a file with invalid JSON content
    invalid_json_file = tmpdir.join("invalid.json")
    invalid_json_file.write("this is not valid JSON content")

    # When & Then: Attempt to read the file and assert it raises a JSONDecodeError
    with pytest.raises(json.JSONDecodeError):
        read_json_as_dict(invalid_json_file.strpath)
