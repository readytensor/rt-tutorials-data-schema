import os
import json

def read_json_in_directory(directory_path: str) -> dict:
    """
    Reads a JSON file in the given directory path as a dictionary and returns the dictionary.
    
    Args:
    - directory_path (str): The path to the directory containing the JSON file.
    
    Returns:
    - dict: The contents of the JSON file as a dictionary.
    
    Raises:
    - ValueError: If no JSON file is found in the directory or if multiple JSON files are found in the directory.
    """
    json_files = [file for file in os.listdir(directory_path) if file.endswith('.json')]
    
    if not json_files:
        raise ValueError('No JSON file found in directory')
    
    if len(json_files) > 1:
        raise ValueError('Multiple JSON files found in directory')
    
    json_file_path = os.path.join(directory_path, json_files[0])
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data
