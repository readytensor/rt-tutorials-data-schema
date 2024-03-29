import pytest
from src.schema.data_schema import BinaryClassificationSchema


def test_init():
    """
    Test the initialization of BinaryClassificationSchema class with a valid schema dictionary.
    Asserts that the properties of the schema object match the input schema dictionary.
    """
    # Given
    schema_dict = {
        "modelCategory": "binary_classification",
        "title": "Test Title",
        "description": "Test Description",
        "schemaVersion": 1.0,
        "inputDataFormat": "CSV",
        "id": {"name": "Test ID"},
        "target": {"name": "Test Target", "classes": ["0", "1"], "nullable": False},
        "features": [{"name": "Test feature", "dataType": "NUMERIC", "nullable": True}]
    }

    # When
    schema = BinaryClassificationSchema(schema_dict)

    # Then
    assert schema.model_category == "binary_classification"
    assert schema.title == "Test Title"
    assert schema.description == "Test Description"
    assert schema.schema_version == 1.0
    assert schema.input_data_format == "CSV"
    assert schema.id == "Test ID"
    assert schema.target == "Test Target"
    assert schema.target_classes == ["0", "1"]
    assert schema.numeric_features == ["Test feature"]
    assert schema.categorical_features == []
    assert schema.features == ["Test feature"]
    assert schema.all_fields == ["Test ID", "Test Target", "Test feature"]


def test_get_allowed_values_for_categorical_feature():
    """
    Test the method to get allowed values for a categorical feature.
    Asserts that the allowed values match the input schema dictionary.
    Also tests for a ValueError when trying to get allowed values for a non-existent feature.
    """
    # Given
    schema_dict = {
        "modelCategory": "binary_classification",
        "title": "Test Title",
        "description": "Test Description",
        "schemaVersion": 1.0,
        "inputDataFormat": "CSV",
        "id": {"name": "Test ID"},
        "target": {"name": "Test Target", "classes": ["0", "1"]},
        "features": [
            {"name": "Test feature 1", "dataType": "NUMERIC", "nullable": True},
            {"name": "Test feature 2", "dataType": "CATEGORICAL", "categories": ["A", "B"], "nullable": True}
        ]
    }
    schema = BinaryClassificationSchema(schema_dict)

    # When
    allowed_values = schema.get_allowed_values_for_categorical_feature("Test feature 2")

    # Then
    assert allowed_values == ["A", "B"]

    # When / Then
    with pytest.raises(ValueError):
        schema.get_allowed_values_for_categorical_feature("Invalid feature")


def test_get_example_value_for_numeric_feature():
    """
    Test the method to get an example value for a numeric feature.
    Asserts that the example value matches the input schema dictionary.
    Also tests for a ValueError when trying to get an example value for a non-existent feature.
    """
    # Given
    schema_dict = {
        "modelCategory": "binary_classification",
        "title": "Test Title",
        "description": "Test Description",
        "schemaVersion": 1.0,
        "inputDataFormat": "CSV",
        "id": {"name": "Test ID"},
        "target": {"name": "Test Target", "classes": ["0", "1"]},
        "features": [
            {"name": "Test feature 1", "dataType": "NUMERIC", "example": 123.45, "nullable": True},
            {"name": "Test feature 2", "dataType": "CATEGORICAL", "categories": ["A", "B"], "nullable": True}
        ]
    }
    schema = BinaryClassificationSchema(schema_dict)

    # When
    example_value = schema.get_example_value_for_feature("Test feature 1")

    # Then
    assert example_value == 123.45

    # When / Then
    with pytest.raises(ValueError):
        schema.get_example_value_for_feature("Invalid feature")


def test_get_description_for_id_target_and_features():
    """
    Test the methods to get descriptions for the id, target, and features.
    Asserts that the descriptions match the input schema dictionary.
    Also tests for a ValueError when trying to get a description for a non-existent feature.
    """
    # Given
    schema_dict = {
        "modelCategory": "binary_classification",
        "title": "Test Title",
        "description": "Test Description",
        "schemaVersion": 1.0,
        "inputDataFormat": "CSV",
        "id": {"name": "Test ID", "description": "ID field"},
        "target": {"name": "Test Target", "description": "Target field", "classes": ["0", "1"]},
        "features": [
            {"name": "Test feature 1", "dataType": "NUMERIC", "description": "Numeric feature", "nullable": True},
            {"name": "Test feature 2", "dataType": "CATEGORICAL",
             "description": "Categorical feature", "categories": ["A", "B"], "nullable": True}
        ]
    }
    schema = BinaryClassificationSchema(schema_dict)

    # When
    id_description = schema.id_description
    target_description = schema.target_description
    feature_1_description = schema.get_description_for_feature("Test feature 1")
    feature_2_description = schema.get_description_for_feature("Test feature 2")

    # Then
    assert id_description == "ID field"
    assert target_description == "Target field"
    assert feature_1_description == "Numeric feature"
    assert feature_2_description == "Categorical feature"

    # When / Then
    with pytest.raises(ValueError):
        schema.get_description_for_feature("Invalid Feature")


def test_is_feature_nullable():
    """
    Test the method to check if a feature is nullable.
    Asserts that the nullable status matches the input schema dictionary.
    Also tests for a ValueError when trying to check the nullable status for a non-existent feature.
    """
    # Given
    schema_dict = {
        "modelCategory": "binary_classification",
        "title": "Test Title",
        "description": "Test Description",
        "schemaVersion": 1.0,
        "inputDataFormat": "CSV",
        "id": {"name": "Test ID", "nullable": False},
        "target": {"name": "Test Target", "classes": ["0", "1"], "nullable": False},
        "features": [
            {"name": "Test feature 1", "dataType": "NUMERIC", "nullable": True},
            {"name": "Test feature 2", "dataType": "CATEGORICAL", "categories": ["A", "B"], "nullable": False}
        ]
    }
    schema = BinaryClassificationSchema(schema_dict)

    # When
    is_nullable = schema.is_feature_nullable("Test feature 1")

    # Then
    assert is_nullable is True

    # When
    is_not_nullable = schema.is_feature_nullable("Test feature 2")

    # Then
    assert is_not_nullable is False

    # When / Then
    with pytest.raises(ValueError):
        schema.is_feature_nullable("Invalid feature")
