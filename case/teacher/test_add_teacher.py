from jiekouxiangmu.case.teacher.add_teacher import *
import allure

@allure.story("添加老师的接口-添加成功")
def test_add_teacher(delete_teacher_sql):
    teacher=AddTeacher(s)
    teacher.login()
    result = teacher.add_teacher(name="yoyo678")
    actul_result = teacher.get_add_teacher(result)
    assert actul_result == "yoyo678"