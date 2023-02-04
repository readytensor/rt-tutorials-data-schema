from schema_provider import BinaryClassificationSchema

def read_schema():
    """Reads the binary classification schema."""

    # path to the schema file
    schema_fpath = "./inputs/titanic_schema.json"

    # instantiate schema provider which loads the json file schema
    bc_schema = BinaryClassificationSchema(schema_fpath)

    # check if schema provider parsed the schema correctly
    print(f"id_field is: `{bc_schema.id_field}`")
    print(f"target_field is: `{bc_schema.target_field}`")
    print(f"target_class is: `{bc_schema.target_class}`")
    print(f"Numerical features are: {bc_schema.numeric_features}")
    print(f"Categorical features are: {bc_schema.categorical_features}")
    print(f"All fields are: {bc_schema.all_fields}")


if __name__ == "__main__":
    read_schema()