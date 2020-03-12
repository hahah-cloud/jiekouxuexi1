import requests
import os
s=requests.session()

os.environ["host"]="http://49.235.92.12:9000"

def register(name):
    url = os.environ["host"]+"/api/v1/register"
    body = {
        "username": name,
        "password": "123456",
        "mail": "7890@qq.com"
    }
    r = s.post(url, body)
    return r.json()



print(register("test"))