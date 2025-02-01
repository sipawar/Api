import requests


class TestHomeTaskSix:

    def test_get_city_weather(self,task,read_ini):
        data = read_ini[task]
        base_url = data['base_url']
        city=data['city']
        api_key=data['api_key']


        url=f"{base_url}?q={city}&appid={api_key}"
        print(url)
        res=requests.get(url)
        assert  res.status_code==200
        res_json=res.json()
        print(f"current status is {res_json['weather']}")
        return res_json['coord']['lon'],res_json['coord']['lat']


    def test_get_details_coord(self, task, read_ini):
        data = read_ini[task]
        base_url = data['base_url']
        city = data['city']
        api_key = data['api_key']
        lon,lat= self.test_get_city_weather(task, read_ini)
        url=f"{base_url}?lat={lat}&lon={lon}&appid={api_key}"
        res=requests.get(url)
        assert  res.status_code==200
        res_json=res.json()

        assert res_json['name'] == 'Hyderabad'
        assert res_json['sys']['country'] == 'IN'
        assert res_json['main']['temp_min'] > 0
        assert res_json['main']['temp_max'] > 0
        print(res_json)