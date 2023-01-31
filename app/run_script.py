from schema_reader import BinaryClassificationSchemaReader


def read_schema(): 
    """Reads the binary classification schema."""

    # path to the schema file
    schema_fpath = "./inputs/employee_attrition_schema.json"

    # instantiate schema_reader which loads the schema
    bc_schema_reader = BinaryClassificationSchemaReader(schema_fpath)
    
    # check if schema_reader parsed the schema correctly
    print(f"id_field is: `{bc_schema_reader.id_field}`")
    print(f"target_field is: `{bc_schema_reader.target_field}`")
    print(f"target_class is: `{bc_schema_reader.target_class}`")
    print(f"Numerical features are: {bc_schema_reader.numeric_features}")
    print(f"Categorical features are: {bc_schema_reader.categorical_features}")
    print(f"All fields are: {bc_schema_reader.all_fields}")




if __name__ == "__main__": 
    read_schema()