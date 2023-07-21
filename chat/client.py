import requests
import json

code = '从微信登录中获取code'

# 获取token
token_url = 'http://localhost:8000/login?code='+code
print(f"Token request URL: {token_url}") # 打印请求URL

r = requests.get(token_url)

print(f"Status code: {r.status_code}") # 打印响应状态码
print(f"Response headers: {r.headers}") # 打印响应头部信息
print(f"Response content: {r.text}") # 打印响应内容

try:
    token = r.json()['token'] # 解析JSON响应
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}") # 打印JSON解析错误
    print(f"Response content: {r.text}") # 打印原始响应内容
    raise

# 保存token
headers = {'Authorization': 'Bearer ' + token}

# 发送消息并打印回复
msg = '你好'
send_url = 'http://localhost:8000/send_message'
print(f"Send message URL: {send_url}") # 打印请求URL

r = requests.post(send_url,
                  json={'message':msg},
                  headers=headers)

print(f"Status code: {r.status_code}") # 打印响应状态码
print(f"Response headers: {r.headers}") # 打印响应头部信息
print(f"Response content: {r.text}") # 打印响应内容

try:
    print(r.json()['response']) # 解析JSON响应并打印回复
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}") # 打印JSON解析错误
    print(f"Response content: {r.text}") # 打印原始响应内容
    raise

# 可以多次发送消息测试
msg2 = '第二条测试消息'
r = requests.post(send_url, json={'message':msg2}, headers=headers)

try:
    print(r.json()['response']) # 解析JSON响应并打印回复
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}") # 打印JSON解析错误
    print(f"Response content: {r.text}") # 打印原始响应内容
    raise
