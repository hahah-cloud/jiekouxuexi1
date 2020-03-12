import pytest
import os
from jiekouxiangmu.case.login.func_login import login
import requests
from jiekouxiangmu.common.connect_mysql import execute_sql

'''注册'''
@pytest.fixture(scope="function")
def delete_user():
    delete_sql = 'delete from auth_user where username="testw";'
    execute_sql(delete_sql)


@pytest.fixture(scope="function")
def login_fix():
    print("---先进行登录---")
    s=requests.session()
    login(s)
    return s

'''删除添加的老师'''
@pytest.fixture(scope="function")
def delete_teacher_sql():
    delete_sql1='delete from djangoweb.hello_teacher where teacher_name="yoyo678";'
    yield
    print("数据清理:测试用例之后执行")
    execute_sql(delete_sql1)



'''环境变量'''
def pytest_addoption(parser):
    parser.addoption(
        "--cmdhost",
        action="store",
        default="http://49.235.92.12:9000",
        help="test case project host address"
    )
    parser.addoption(
        "--teacherhost",
        default="http://http://49.235.92.12:8020"
    )

@pytest.fixture(scope="session",autouse=True)
def host(request):
    '''获取命令行参数，给到环境变量'''
    os.environ["host"]=request.config.getoption("--cmdhost")
    print("当前环境为%s"%os.environ["host"])
    os.environ["--teacherhost"]=request.config.getoption("--teacherhost")
    print("当前环境变量:%s"%os.environ["--teacherhost"])





