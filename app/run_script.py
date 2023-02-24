
from data_management.schema_provider import BinaryClassificationSchema
import paths

def read_schema():
    """Reads the binary classification schema."""

    # instantiate schema provider which loads the json file schema
    data_schema = BinaryClassificationSchema(paths.SCHEMA_FPATH)

    # check if schema provider parsed the schema correctly
    print(f"id_field is: `{data_schema.id_field}`")
    print(f"target_field is: `{data_schema.target_field}`")
    print(f"target_class is: `{data_schema.target_class}`")
    print(f"Numerical features are: {data_schema.numeric_features}")
    print(f"Categorical features are: {data_schema.categorical_features}")
    print(f"All fields are: {data_schema.all_fields}")


if __name__ == "__main__":
    read_schema()