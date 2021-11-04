import requests
import base64
import re
from PIL import ImageFont, Image, ImageDraw
import argparse
from fontTools.ttLib.ttFont import TTFont
import os
from fontTools.ttLib import TTFont
from lxml import etree
from hashlib import md5
import shutil
shutil.rmtree('tudiimg')
os.mkdir('tudiimg')
url = 'https://www.china.cn/leddengdai/4255707828.html'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
ret = requests.get(url=url,headers=headers)


# with open('china.html','w',encoding='utf8') as f:
#     f.write(ret.text)
#
# with open('china.html','r',encoding='utf8') as f:
#     ret = f.read()
ba64 = re.findall('base64,(.*?)\'\) forma',ret.text)[0]

b= base64.b64decode(ba64)

def uni_2_png(txt,name, filename, img_size=512):
    img = Image.new('1', (img_size, img_size), 255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(filename, int(img_size * 0.7))

    txt = chr(txt)
    x, y = draw.textsize(txt, font=font)
    draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
    # draw.text((0,0), txt, font=font, fill=0)
    file_name = '%s/%s.png' % ('tudiimg', name)
    img.save(file_name)


def to_pic(filename):
    import time
    import os
    import requests
    all_name_dict = {}
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=m3L74UXjhYguSZeZpOzOp0Km&client_secret=in3GNQiBt4jjeSNoeXotoDxtVQ4vzRB3'
    response = requests.get(host)
    if response:
        access_token = response.json()["access_token"]
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"
    file_list = os.listdir(f'./{filename}')
    for name in file_list:

        # 二进制方式打开图片文件
        f = open(f'.\\{filename}\\{name}', 'rb')
        img = base64.b64encode(f.read())

        params = {"image": img}
        access_token = access_token
        request_url = request_url + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        for i in range(1,8):

            response = requests.post(request_url, data=params, headers=headers)
            if response:
                if 'error_code' not in response.json():
                    words_result = response.json().get("words_result")[0].get("words")
                    all_name_dict[name.strip('.png')] = words_result

                    break
    return all_name_dict
            # response = response.json(), name
            # yield response

with open('2.woff','wb') as f:
    f.write(b)
font = TTFont('2.woff')
font.saveXML('21.xml')

font = TTFont('2.woff')

cmap = font.getBestCmap()
for key, value in cmap.items():
    uni_2_png(key, value.strip("uni"),'2.woff')


all_num_reslut = to_pic('tudiimg')
print(all_num_reslut)
# print(response,name)
# with open('2.xml','r',encoding='utf8') as f:
#     ret = f.read()
# ret = ret.replace('\n','').replace(' ','')
#
# font_cmap = {}
# for i in cmap:
#     data = re.findall(f'<CharStringname="{cmap[i]}">(.*?)</CharString>', ret)[0]
#     char_md5 = md5(data.encode('utf8')).hexdigest()
#     for k in font_dict:
#         if k==char_md5:
#             font_cmap['&#x'+cmap[i][3:]+';']=font_dict[k]
# print(font_cmap)
#
# with open('china.html','r',encoding='utf8') as f:
#     ret = f.read()
# for i in font_cmap:
#     ret = ret.replace(i,str(font_cmap[i]))
# page_html = etree.HTML(ret)
# phone = page_html.xpath('/html//div[5]/div[2]/div[3]/div[1]/div[3]/span[1]/text()')
# numb = page_html.xpath('/html//div[5]/div[2]/div[3]/div[1]/div[3]/span[2]/text()')
#
# print(phone,numb)

