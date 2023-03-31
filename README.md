## Introduction

This repository demonstrates how to use data schemas to create adaptable machine learning algorithm implementations. By using data schemas, you can avoid hard-coding your implementation to a specific dataset, which can make it easier to apply your algorithms to new datasets in the future.

## Repository Contents

The `app/` folder in the repository contains the following:

- `inputs/`: a folder containing sub-folders for schema and training/testing data. An example schema file called `titanic_schema.json` is placed in `inputs/data_config/`.
- `data_management/` contains a script called `schema_provider.py` which has the **BinaryClassificationSchemaReader** class. This class can be used to parse a data schema and extract relevant information from it. Directory also contains a script called `data_utils.py` which contains a function to read a json file with any name from a given directory.
- `paths.py`: script contains variables which represent various paths to be used in the repository.
- `run_script.py`: an example script that uses the **BinaryClassificationSchemaReader** class to parse an example schema file and print out information about the fields and features in the schema.

## Example Schema File

An example schema file called `titanic_schema.json` is included in the `inputs/data_config` folder of this repository. The schema is created as per Ready Tensor specifications for the Binary Classification problem category. This file serves as an example of the format that a data schema can follow and provides a basis for users to create their own schema files for their own datasets.

## Usage

The repository contains a single Python class, **BinaryClassificationSchemaReader**, which reads a JSON data schema file and extracts information about the features and target variables of a binary classification problem.

To use the **BinaryClassificationSchemaReader** class, instantiate it by passing the file path of the data schema. Then, access the following properties to get the information about the features and target variables:

- `id_field`: the ID field of the data
- `target_field`: the target field of the data
- `target_class`: the target class of the binary classification problem
- `numeric_features`: the list of numerical features in the data
- `categorical_features`: the list of categorical features in the data
- `features`: the list of all features in the data
- `all_fields`: the list of all fields in the data, including the ID and target fields

For more details, see the code and the provided example in the `read_schema` function in `run_script.py` file. To run the code, simply run the script as follows.

```bash
python app/run_script.py

```

The function prints the contents of the schema file, including the `id_field`, `target_field`, `target_class`, `numeric_features`, `categorical_features`, and `all_fields`.
