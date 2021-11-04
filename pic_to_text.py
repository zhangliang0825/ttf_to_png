
# encoding:utf-8
import time

import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=m3L74UXjhYguSZeZpOzOp0Km&client_secret=in3GNQiBt4jjeSNoeXotoDxtVQ4vzRB3'
response = requests.get(host)
if response:
    access_token = response.json()["access_token"]
    print(access_token)
# encoding:utf-8

import requests
import base64
import os
'''
通用文字识别（高精度版）
'''
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"
file_list = os.listdir('./imgs')
for name in file_list:
    time.sleep(1)
# 二进制方式打开图片文件
    f = open(f'.\imgs\\{name}', 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    access_token = access_token
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json(),name)