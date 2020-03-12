import requests
import re
from lxml import etree
from requests_toolbelt import MultipartEncoder
import allure

s=requests.session()

@allure.feature("添加老师接口")
class AddTeacher():


    @allure.step("添加老师的接口--登录成功")
    def login(self):
        url="http://49.235.92.12:8020/xadmin/"
        r1=s.get(url)
        #print(r1.text)
        cookie=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r1.text)
        print(cookie[0])
        body={
            "csrfmiddlewaretoken": cookie[0],
            "username":"admin",
            "password":"yoyo123456",
            "this_is_the_login_form":"1",
            "next":"/xadmin/"
        }
        r2=s.post(url,body)
        #print(r2.text)
        if "主页面 | 后台页面" in r2.text:
            print("登录成功")
        else:
            print("登录失败")


    @allure.step("添加老师的接口--添加老师")
    def add_teacher(self,name):
        url2="http://49.235.92.12:8020/xadmin/hello/teacher/add/"
        r3=s.get(url2)
        cookie1=re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r3.text)
        m=MultipartEncoder(
            fields=[
                ("csrfmiddlewaretoken",cookie1[0]),
                ("csrfmiddlewaretoken",cookie1[0]),
                ("teacher_name",name),
                ("tel","111"),
                ("mail","7889@qq.com"),
                ("sex","M"),
                ("_save","")]
        )
        r4=s.post(url2,data=m,headers={"Content-Type":m.content_type})
        return r4.text

    @allure.step("添加老师的接口--验证是否添加成功")
    def get_add_teacher(self,result):
        demo=etree.HTML(result)
        nodes=demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
        #print(nodes[0].text)
        return nodes[0].text



if __name__ == '__main__':
    shili=AddTeacher()
    shili.login()
    result=shili.add_teacher(name="yoyo678")
    actul_result=shili.get_add_teacher(result)
    assert actul_result=="yoyo678"