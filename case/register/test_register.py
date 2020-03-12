from jiekouxiangmu.case.register.register import register
import allure

@allure.story("注册接口-注册成功")
def test_register(delete_user):
    result=register(name="testw")
    print(result)
    assert result["msg"] == '注册成功!'

@allure.story("注册接口-用户已被注册")
def test_register_2():
    result2=register(name="testw")
    print(result2)
    assert result2["msg"] == 'testw用户已被注册'