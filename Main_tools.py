from urllib.parse import quote, unquote
import base64
import re
import binascii
import requests

def u(value):
    print("编码后："+quote(value))
def ul(value):
    print("解码后："+unquote(value))
def base(value):
    b = str(value)
    bs64_e = base64.b64encode(b.encode('utf-8'))
    bs64_e = str(bs64_e)
    # print(bs64_e)
    obj = re.compile(r"b'(?P<bs>.*?)'", re.S)
    for i in obj.finditer(bs64_e):
        print("编码后："+i.group("bs"))
def Base(value):
    b = str(value)
    bs64_d = str(base64.b64decode(b),'utf-8')
    print("解码后："+bs64_d)
def hex(value):
    h = bytes(value, encoding="utf-8")
    he = str(binascii.b2a_hex(h))
    obj = re.compile(r"b'(?P<hex>.*?)'", re.S)
    for i in obj.finditer(he):
        print("编码后："+"0x"+i.group("hex"))
def Hex():
    hs = "0x3a".replace("0x", "").replace("0X","")
    h = bytes(hs, encoding="utf-8")
    he = str(binascii.a2b_hex(h))
    obj = re.compile(r"b'(?P<hex>.*?)'", re.S)
    for i in obj.finditer(he):
        print("解码后："+i.group("hex"))
def ascii(value):
    print("编码后：",ord(value))

def Ascii(value):
    print("解码后：",chr(value))
def time(value):
    url = f"http://md5.mmkey.com/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0",

    }
    data = {
        "md5": value,
        "sha256": "",
        "lx": "chkmysql",
        "chkmd5": "%B2%E9%D1%AF"
    }
    resp = requests.post(url, headers=header, data=data)
    resp.encoding = 'gb2312'
    # print(resp.text)
    obj = re.compile(r"<center><font color=red size=3>(?P<md5>.*?) <", re.S)
    for i in obj.finditer(resp.text):
        print(i.group("md5"))
def Time(value):
    url = "https://md5jiami.bmcx.com/web_system/bmcx_com_www/system/file/md5jiami/data/?ajaxtimestamp=1691484970729"
    data = {
        "md5_zifu": value
    }
    resp = requests.post(url, data=data)
    # print(resp.text)
    obj = re.compile(r'style="word-wrap:break-word;">(?P<md5>.*?)</td></tr>', re.S)
    for i in obj.finditer(resp.text):
        print("加密后：",i.group("md5"))

