import os
import json
from typing import Dict

from data_management.schema_provider import BinaryClassificationSchema


def read_json_as_dict(input_path: str) -> Dict:
    """
    Reads a JSON file and returns its content as a dictionary.
    If input_path is a directory, the first JSON file in the directory is read.
    If input_path is a file, the file is read.

    Args:
        input_path (str): The path to the JSON file or directory containing a JSON file.

    Returns:
        dict: The content of the JSON file as a dictionary.

    Raises:
        ValueError: If the input_path is neither a file nor a directory.

    """
    if os.path.isdir(input_path):
        # Get the first JSON file in the directory
        json_file_path = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith('.json')][0]

    elif os.path.isfile(input_path):
        json_file_path = input_path
    else:
        raise ValueError("Input path is neither a file nor a directory")

     # Read the JSON file and return it as a dictionary
    with open(json_file_path, 'r', encoding="utf-8") as file:
        json_data_as_dict = json.load(file)

    return json_data_as_dict


def load_data_schema(schema_dir_path:str) -> BinaryClassificationSchema:
    """
    Load the JSON file schema into a dictionary and instantiate the schema provider.

    Args:
    - df (pd.DataFrame): The pandas dataframe to be saved.

    Returns:
        BinaryClassificationSchema: An instance of the BinaryClassificationSchema.
    """
    schema_dict = read_json_as_dict(input_path=schema_dir_path)
    data_schema = BinaryClassificationSchema(schema_dict)
    return data_schema


