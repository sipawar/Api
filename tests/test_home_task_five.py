
import requests

class TestHomeTaskFive:

    def test_get_count_employees(self,task,read_ini):
        data=read_ini[task]
        base_url=f"{data['base_url']}/employees"
        print(base_url)
        res=requests.get(url=base_url,verify=False)
        print(res.content)
        # cnt=len(res.json())
        # print(cnt)
        print(res.status_code)
        print(res.headers['content-type'])


    def test_create_new_employee(self,read_ini,task):

        data=read_ini[task]
        base_url=f"{data['base_url']}/create"
        data=	{"name":"test","salary":"123","age":"23"}

        res=requests.post(url=base_url,json=data,verify=False)
        print(res.status_code)
        print(res.content)


