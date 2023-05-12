# Adaptable ML - Data Schemas

## Project Description

This repository is part of a comprehensive tutorial series aimed at building adaptable machine learning models. It specifically corresponds to the "Using Data Schemas" tutorial. The primary goal of this tutorial, and by extension this repository, is to demonstrate how data schemas can be effectively leveraged to construct flexible machine learning implementations, thereby eliminating the need for hard-coding to specific datasets. By following the strategies outlined here, AI developers can create reusable, domain-agnostic algorithms and thereby enhance the versatility and applicability of their machine learning models.

## Project Structure

```bash
├── inputs/
│   ├── data/
│   │   ├── testing/
│   │   └── training/
│   └── schema/
├── model/
│   └── artifacts/
├── outputs/
│   ├── hpt_outputs/
│   ├── logs/
│   └── predictions/
├── src/
│   ├── config/
│   ├── data_model/
│   ├── hyperparameter_tuning/
│   ├── prediction/
│   ├── preprocessing/
│   ├── schema/
│   └── xai/
├── tests/
│   ├── <mirrors `/src` structure ...>
│   ...
│   ...
├── tmp/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

- **`/inputs`**: This directory contains all the input files for your project, including the data and schema files. The data is further divided into testing and training subsets.
- **`/model/artifacts`**: This directory is used to store the model artifacts, such as trained models and their parameters.
- **`/outputs`**: The outputs directory contains all output files, including the prediction results, logs, and hyperparameter tuning outputs.
- **`/src`**: This directory holds the source code for the project. It is further divided into various subdirectories such as `config` for configuration files, `data_model` for data models for input validation, `hyperparameter_tuning` for hyperparameter-tuning (HPT) related files, `prediction` for prediction model scripts, `preprocessing` for data preprocessing scripts, `schema` for schema scripts, and `xai` for explainable AI scripts.
- **`/tests`**: This directory contains all the tests for the project. It mirrors the `src` directory structure for consistency.
- **`/tmp`**: This directory is used for storing temporary files which are not necessary to commit to the repository.
- **`.gitignore`**: This file specifies the files and folders that should be ignored by Git.
- **`LICENSE`**: This file contains the license for the project.
- **`README.md`**: This file contains the documentation for the project, explaining how to set it up and use it.
- **`requirements.txt`**: This file lists the dependencies for the project, making it easier to install all necessary packages.

## Installation / Setup Instructions

Describe how to get the project setup. Include any dependencies that need to be installed. If it's a Docker container, include instructions for building and running the Docker container.

## Requirements

Specify any system requirements or prerequisite knowledge for using your project. This could include the programming language version, any necessary libraries, or specific hardware requirements.

## Usage Instructions

Describe how to use your project. Include any relevant code snippets or examples.

## API Reference/Documentation

If your project is an API, include a link to the API reference or documentation.

## Testing

Describe how to run the tests for your project.

## License

Include a section detailing the license your project is under. Do this even if the actual license is in a separate file. This section doesn't need to contain the full text of the license - instead, it can be a brief summary of the license and a reference to the separate LICENSE file.

## Contact Information

Include contact information for the maintainer(s) of the project. This could be an email address, a link to a GitHub profile, or a link to a LinkedIn profile.
