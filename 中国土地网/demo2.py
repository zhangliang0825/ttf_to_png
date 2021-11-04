import requests
import base64
import re
from fontTools.ttLib import TTFont
from lxml import etree
from hashlib import md5
url = 'http://szsyxfp.b2b.huangye88.com/company_contact.html'
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36'
}
ret = requests.get(url=url,headers=headers)


with open('china1.html','w',encoding='utf8') as f:
    f.write(ret.text)

with open('china1.html','r',encoding='utf8') as f:
    ret = f.read()

ba64 = re.findall('base64,(.*?)"\) format',ret,re.S)[0]
b= base64.b64decode(ba64)
with open('3.woff','wb') as f:
    f.write(b)
font = TTFont('3.woff')
font.saveXML('3.xml')

# num_list = [1,3,5,7,8,2,9,0,'-',4]
# font_dict = {
#     '0072296251cdc1cf39f36bfe71030516':1,
#     'ad2cb8eb87212068a1f5fcd890decfad':3,
#     '13164316728f72504c55a2ffb0e0c495':5,
#     '168b3dc2e5f487ac5d2921af154182e1':7,
#     'b651cdcb5c2a4234204c3219fb9bb82f':8,
#     'f1d930f3bf8e87dd52e3b92c5bf5fdd7':2,
#     'a6a070db8e1d3d6af10e04b203323641':9,
#     '5b46b9d4d383db9e425efcfd2dd53cd9':0,
#     '7edd56fae59e9cabd2655f138f2c0925':'-',
#     'accd825aab52df41a5bc6701ff2156a6':6,
#     'bf4e2e8facb4a13551e6ee343f44c022':4,
#
# }
# font = TTFont('2.woff')
# cmap = font.getBestCmap()
# print(cmap)
# with open('2.xml','r',encoding='utf8') as f:
#     ret = f.read()
# ret = ret.replace('\n','').replace(' ','')
#
# font_cmap = {}
# for i in cmap:
#
#     data = re.findall(f'<CharStringname="{cmap[i]}">(.*?)</CharString>', ret)[0]
#     print(data)
#     char_md5 = md5(data.encode('utf8')).hexdigest()
#     print(char_md5)
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

