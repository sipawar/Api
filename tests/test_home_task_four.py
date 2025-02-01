import requests
class TestHomeTaskFour:

    def test_get_details(self,task,read_ini):

        data=read_ini[task]
        base_url=data['base_url']
        response=requests.get(base_url)
        response_json=response.json()
        print(response_json)
        assert response.status_code==200
        assert len(response_json) >3
        found = any(item['name'] == 'Ervin Howell' for item in response_json)
        assert found, "Expected to find a person named 'Ervin Howell' in the response data."