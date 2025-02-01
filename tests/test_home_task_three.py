import requests
import pytest


class TestHome_task_three:


    def test_create_pet(self,read_ini,task):
        """Test to create a pet and verify it's created correctly."""
        pet_data={
            "id": 12345,
            "category": {"id": 1, "name": "dog"},
            "name": "snoopie",
            "photoUrls": ["string"],
            "tags": [{"id": 0, "name": "string"}],
            "status": "pending"}
        data=read_ini[task]
        base_url=data['base_url_post']
        response = requests.post(base_url, json=pet_data)
        assert response.status_code == 200
        print(response.json())

    def test_get_pet(self,read_ini,task):
        """Test to get a pet and validate properties."""
        data=read_ini[task]
        base_url=data['base_url_get']

        response = requests.get(f"{base_url}")
        assert response.status_code == 200
        assert response.headers['Content-Type'] in 'application/json; charset=utf-8'

        pet = response.json()
        assert pet['category']['name'] == 'dog'
        assert pet['name'] == 'snoopie'
        assert pet['status'] == 'pending'