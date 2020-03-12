import allure
import pytest
from jiekouxiangmu.common.read_yml import *
import os


@allure.feature("修改信息接口")
class TestUpdateInfo():

    @allure.story("修改信息成功")
    def test_fix_info_1(self,login_fix):
        url = os.environ["host"] + "/api/v1/userinfo"
        s=login_fix
        body = {
            "name": "test",
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"
        }
        r=s.post(url,body)
        print(r.json())
        assert r.json()["message"]=='update some data!'
        assert r.json()["code"]==0
        return r.json()["message"]



    @allure.story("修改信息-修改姓名成不符合的字段")
    @pytest.mark.parametrize("test_input",["中文啦啦啦"," ","&**())%%$#@@$","00000","TTYIooaowoowowowowoowoooooooo"])
    def test_info_name(self,login_fix,test_input):
        url = os.environ["host"] + "/api/v1/userinfo"
        s=login_fix
        body = {
            "name":test_input,
            "sex": "M",
            "age": 20,
            "mail": "283340479@qq.com"
        }
        r=s.post(url,body)
        print(r.json())
        assert r.json()["message"]=="无权限操作"
        assert r.json()["code"]==4000



    ymlPath=path()
    test_data=readyml(ymlPath)["update_info_sex"]
    @allure.story("修改信息-修改性别成不符合的字段")
    @pytest.mark.parametrize("test_input_sex,expect",test_data)
    def test_info_sex(self,login_fix,test_input_sex,expect):
        url = os.environ["host"] + "/api/v1/userinfo"
        s=login_fix
        body = {
            "name":"test",
            "sex": test_input_sex,
            "age": 20,
            "mail": "283340479@qq.com"
        }
        r=s.post(url,body)
        print(r.json())
        assert r.json()["message"]==expect["message"]

    @allure.story("修改信息-修改年龄成不符合的字段")
    @pytest.mark.parametrize("test_input_age",[" ","jdeidjiia",34.89])
    def test_info_age(self,login_fix,test_input_age):
        url = os.environ["host"] + "/api/v1/userinfo"
        s=login_fix
        body = {
            "name":"test",
            "sex": "M",
            "age":test_input_age,
            "mail": "283340479@qq.com"
        }
        r=s.post(url,body)
        print(r.json())
        assert r.json()["message"]=='参数类型错误'

    @allure.story("修改信息-修改邮箱成不符合的字段")
    @pytest.mark.parametrize("test_input_mail",[" ","中文件都觉得","72882999$%%%^^^6"])
    def test_info_mail(self,login_fix,test_input_mail):
        url = os.environ["host"] + "/api/v1/userinfo"
        s=login_fix
        body = {
            "name":" ",
            "sex": "M",
            "age": 20,
            "mail": test_input_mail
        }
        r=s.post(url,body)
        print(r.json())
        assert r.json()["message"]=='无权限操作'


    test_data_2=readyml(ymlPath)["update_info_2"]
    @allure.story("修改信息-修改各个字段，修改成不同的情况，查看响应")
    @pytest.mark.parametrize("name,sex,age,mail,expect",test_data_2)
    def test_fix_info_2(self,login_fix,name,sex,age,mail,expect):
        url = os.environ["host"] + "/api/v1/userinfo"
        s = login_fix
        body = {
            "name": name,
            "sex": sex,
            "age": age,
            "mail": mail
        }
        r = s.post(url, body)
        print(r.json())
        assert r.json()["message"]==expect["message"]


    # '''传参---入参'''
    # def test_fix_info_3(login_fix):
    #     url = os.environ["host"] + "/api/v1/userinfo"
    #     s = login_fix
    #     b=test_fix_info_1(login_fix)
    #     body = {
    #         "name": b,
    #         "sex": "M",
    #         "age": 20,
    #         "mail": "18811487508@qq.com"
    #     }
    #     r = s.post(url, body)
    #     print(body)

