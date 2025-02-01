import requests
import pytest

# Fixture for validating response, consuming expected_code as input
def validate_response(response, expected_code):
    assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"
    assert response.json(), "Response contains no JSON data"

# Testing class using `base_url` and each resource in `resources`

class TestResourceOperations:

    def test_get_specific_resource(self, resource,read_ini,task):
        data=read_ini[task]
        base_url=data['base_url']
        response = requests.get(f"{base_url}{resource}/1")
        validate_response(response, 200)

    def test_modify_specific_resource(self, resource,read_ini,task):
        data=read_ini[task]
        base_url=data['base_url']
        modified_data = {'title': 'new value','body': 'New content', 'userId': 1}
        response = requests.put(f"{base_url}{resource}/1", json=modified_data)
        validate_response(response, 200)

    def test_delete_specific_resource(self, resource,read_ini,task):
        data = read_ini[task]
        base_url = data['base_url']
        response = requests.delete(f"{base_url}{resource}/1")
        validate_response(response, 200)  # Adjust status code based on actual API behavior, could be 204

    def test_create_resource(self, resource,read_ini,task):
        data = read_ini[task]
        base_url = data['base_url']
        new_data = {'title': 'New Entry', 'body': 'New content', 'userId': 1}
        response = requests.post(f"{base_url}{resource}", json=new_data)
        validate_response(response, 201)
