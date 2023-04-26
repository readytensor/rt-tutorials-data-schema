
from utils import load_data_schema
from config import paths


def read_schema():
    """Reads the binary classification schema."""

    # load the json file schema into a dictionary and use it to instantiate the schema provider
    data_schema = load_data_schema(paths.SCHEMA_DIR)

    # check if schema provider parsed the schema correctly
    print(f"id_field is: `{data_schema.id_field}`")
    print(f"target_field is: `{data_schema.target_field}`")
    print(f"positive_class is: `{data_schema.positive_class}`")
    print(f"Numerical features are: {data_schema.numeric_features}")
    print(f"Categorical features are: {data_schema.categorical_features}")
    print(f"Allowed values for Categorical features are: {data_schema.allowed_categorical_values}")
    print(f"All fields are: {data_schema.all_fields}")


if __name__ == "__main__":
    read_schema()