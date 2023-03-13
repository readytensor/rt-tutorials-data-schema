import os


# Path to the current file's directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to inputs inside ml_vol
INPUT_DIR = os.path.join(CURRENT_DIR, "inputs")

# File path for input schema file 
SCHEMA_DIR = os.path.join(INPUT_DIR, "data_config")

