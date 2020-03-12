import requests

s=requests.session()
url="http://49.235.92.12:9000/api/v1/login"

def login(s):
    body = {
        "username": "test",
        "password": "123456"
    }
    r=s.post(url,body)
    token=r.json()["token"]
    h={
        "Authorization":"Token %s" %token
    }
    s.headers.update(h)
    print(s.headers)




def unlogin():
    body={
        "username": "test",
        "password": "1234568900"
    }
    r=s.post(url,body)
    return r.json()

if __name__ == '__main__':
    login()
    print(unlogin())