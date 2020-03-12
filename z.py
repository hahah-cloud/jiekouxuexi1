import json
import requests
#会话
s=requests.session()
s.headers.update({'Token': '678d4a99d30122790651bcbdb58fa8cb'})
print(s.headers)


print('----第一个是查学校')

