# Adaptable ML - Data Schemas

## Project Description

This repository is part of a comprehensive tutorial series aimed at building adaptable machine learning models. It specifically corresponds to the "Using Data Schemas" tutorial. The primary goal of this tutorial, and by extension this repository, is to demonstrate how data schemas can be effectively leveraged to construct flexible machine learning implementations, thereby eliminating the need for hard-coding to specific datasets. By following the strategies outlined here, AI developers can create reusable, domain-agnostic algorithms and thereby enhance the versatility and applicability of their machine learning models.

## Project Structure

```bash
binary_class_project/
├── examples/
│   ├── titanic_schema.json
│   ├── titanic_train.csv
│   └── titanic_test.csv
├── inputs/
│   ├── data/
│   │   ├── testing/
│   │   └── training/
│   └── schema/
├── model/
│   └── artifacts/
├── outputs/
│   ├── errors/
│   ├── hpt_outputs/
│   └── predictions/
├── src/
│   ├── config/
│   ├── data_models/
│   ├── hyperparameter_tuning/
│   ├── prediction/
│   ├── preprocessing/
│   ├── schema/
│   │   ├── __init__.py
│   │   └── data_schema.py
│   ├── xai/
│   ├── __init__.py
│   ├── check_schema.py
│   └── utils.py
├── tests/
│   ├── integration_tests/
│   ├── performance_tests/
│   └── unit_tests/
│       ├── <mirrors /src structure>
│       └── ...
├── tmp/
├── .gitignore
├── LICENSE
├── pytest.ini
├── README.md
└── requirements.txt
└── requirements-test.txt
```

- **`/examples`**: This directory contains example files for the titanic dataset. Three files are included: `titanic_schema.json`, `titanic_train.csv` and `titanic_test.csv`. You can place these files in the `inputs/schema`, `inputs/data/training` and `inputs/data/testing` folders, respectively.
- **`/inputs`**: This directory contains all the input files for your project, including the data and schema files. The data is further divided into testing and training subsets.
- **`/model/artifacts`**: This directory is used to store the model artifacts, such as trained models and their parameters.
- **`/outputs`**: The outputs directory contains sub-directories for error logs, and hyperparameter tuning outputs, and prediction results. Note that model artifacts should not be saved in this directory. Instead, they should be saved in the `/model/artifacts` directory.
- **`/src`**: This directory holds the source code for the project. It is further divided into various subdirectories such as `config` for configuration files, `data_models` for data models for input validation, `hyperparameter_tuning` for hyperparameter-tuning (HPT) related files, `prediction` for prediction model scripts, `preprocessing` for data preprocessing scripts, `schema` for schema scripts, and `xai` for explainable AI scripts.
  - Check the `src/schema/data_schema.py` file for the data schema implementation.
- **`/tests`**: This directory contains all the tests for the project. It contains sub-directories for specific types of tests such as unit tests, integration tests, and performance tests. For unit tests, the directory structure mirrors the `/src` directory structure.
- **`/tmp`**: This directory is used for storing temporary files which are not necessary to commit to the repository.
- **`.gitignore`**: This file specifies the files and folders that should be ignored by Git.
- **`LICENSE`**: This file contains the license for the project.
- **`README.md`**: This file contains the documentation for the project, explaining how to set it up and use it.
- **`requirements.txt`**: This file lists the dependencies for the project, making it easier to install all necessary packages.

## Usage

- Create your virtual environment and install dependencies listed in `requirements.txt`.
- Move the three example files (`titanic_schema.json`, `titanic_train.csv` and `titanic_test.csv`) into the `inputs/schema`, `inputs/data/training` and `inputs/data/testing` folders, respectively.
- To run the code, simply run the script as follows.

```bash
python src/check_schema.py
```

## Requirements

Dependencies are listed in the file `requirements.txt`. These packages can be installed by running the following command:

```python
pip install -r requirements.txt
```

For testing, dependencies are listed in the file `requirements-test.txt`. You can install these packages by running the following command:

```python
pip install -r requirements-test.txt
```
