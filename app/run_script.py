
from data_management.schema_provider import BinaryClassificationSchema
from data_management.data_utils import read_json_in_directory
import paths


def read_schema():
    """Reads the binary classification schema."""

    # loads the json file schema into a dictionary and use it to instantiate the schema provider
    schema_dict = read_json_in_directory(paths.SCHEMA_DIR)
    data_schema = BinaryClassificationSchema(schema_dict)

    # check if schema provider parsed the schema correctly
    print(f"id_field is: `{data_schema.id_field}`")
    print(f"target_field is: `{data_schema.target_field}`")
    print(f"target_class is: `{data_schema.target_class}`")
    print(f"Numerical features are: {data_schema.numeric_features}")
    print(f"Categorical features are: {data_schema.categorical_features}")
    print(f"All fields are: {data_schema.all_fields}")


if __name__ == "__main__":
    read_schema()