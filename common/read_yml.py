import yaml
import os

def readyml(ymlPath):
    if not os.path.isfile(ymlPath):
        raise FileNotFoundError("路径不存在")
    f=open(ymlPath,"r",encoding="utf-8")
    cfg=f.read()
    print(type(cfg))
    d=yaml.load(cfg)
    print(type(d))
    print("读取的数据信息是%s"%d)
    return d

def path():
    curPath = os.path.dirname(os.path.realpath(__file__))
    yamPath = os.path.join(curPath, "test_data.yml")
    return yamPath

if __name__ == '__main__':
    # test_data=readyml("test_data.yml")["update_info_sex"]
    # print(test_data)
    # ymlPath=path()
    # print(ymlPath)
    test_data = readyml("test_data.yml")["update_info_2"]
    print(test_data)
