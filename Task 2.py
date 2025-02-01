import requests
import pytest

BASE_URL = 'https://jsonplaceholder.typicode.com'
RESOURCES = ['/posts', '/comments', '/albums', '/photos', '/todos', '/users']

# Function to aid in checking the response validity
def validate_response(response, expected_code):
    assert response.status_code == expected_code, f"Expected {expected_code}, got {response.status_code}"
    assert response.json(), "Response contains no JSON data"



@pytest.mark.parametrize("resource", RESOURCES)
class TestResourceOperations:

    def test_get_specific_resource(self, resource):
        response = requests.get(BASE_URL + f"{resource}/1")
        validate_response(response, 200)

    def test_modify_specific_resource(self, resource):
        modified_data = {'title': 'new value'}  # More specific example data
        response = requests.put(BASE_URL + f"{resource}/1", json=modified_data)
        validate_response(response, 200)

    def test_delete_specific_resource(self, resource):
        response = requests.delete(BASE_URL + f"{resource}/1")
        validate_response(response, 200)  # Adjust according to actual API behavior, sometimes can be 204

    def test_create_resource(self, resource):
        new_data = {'title': 'New Entry', 'body': 'New content', 'userId': 1}  # Tailored example data
        response = requests.post(BASE_URL + resource, json=new_data)
        validate_response(response, 201)
