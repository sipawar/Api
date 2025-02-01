import json
from jsonschema import validate, ValidationError

# Define the JSON schema
schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"},
        "email": {
            "type": "string",
            "format": "email"
        }
    },
    "required": ["name", "age", "email"]
}

# Define a valid example JSON object
valid_data = {
    "name": "John Doe",
    "age": 30,
    "email": "john.doe@example.com"
}

# Define an invalid example JSON object
invalid_data = {
    "name": "John Doe",
    "age": "thirty",  # Invalid data type for "age"
    "email": "john.doe@example.com"
}

# Validate the valid data
try:
    validate(instance=valid_data, schema=schema)
    print("Valid data passed validation.")
except ValidationError as e:
    print("Valid data failed validation:", e)

# Validate the invalid data
try:
    validate(instance=invalid_data, schema=schema)
    print("Invalid data passed validation.")
except ValidationError as e:
    print("Invalid data failed validation:", e)
