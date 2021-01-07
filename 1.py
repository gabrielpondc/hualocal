import pymysql
import requests
import json
import time, datetime
import geocoder
import urllib.request, urllib.parse, urllib.error
import ssl
import os
from urllib.parse import unquote
from bs4 import BeautifulSoup
from lxml import html
import xml.etree.ElementTree as ET
def timestamp_to_date(time_stamp, format_string="%Y-%m-%d %H:%M:%S"):
    time_array = time.localtime(time_stamp)
    str_date = time.strftime(format_string, time_array)
    return str_date
conn = pymysql.connect( # 创建数据库连接
    host='gabrielpondc.softether.net', # 要连接的数据库所在主机ip
    user='root', # 数据库登录用户名
    password='gjk19961226', # 登录用户密码
    database='myloc', # 连接的数据库名，也可以后续通过cursor.execture('user test_db')指定
    charset='utf8mb4' # 编码，注意不能写成utf-8
)
cookies = {
    'c2f61647bf394f4f8f6a2dd4faf2ff74': 'WyIyOTkxMjcxNjk2Il0',
    'HW_id_hicloudportal_2_cloud_huawei_com': 'ae79d1c2c16e4ce3a676e7f32501899b',
    'HW_idts_hicloudportal_2_cloud_huawei_com': '1608729011461',
    'HW_idn_hicloudportal_2_cloud_huawei_com': 'b4c5a80973e1470d8df359219e18eafe',
    'HuaweiID_CAS_ISCASLOGIN': 'true',
    'CASLOGINSITE': '1',
    'LOGINACCSITE': '1',
    'HW_viewts_hicloudportal_2_cloud_huawei_com': '1608729090814',
    'siteID': '1',
    'loginID': '02211CD8B18B21194529C02BDDCD45ED',
    'token': '454364eda0fe766e8e867d8fbd28790ce56956752a4e6cac',
    'cplang': 'zh-cn',
    'isLogin': '1',
    'loginSecLevel': '0',
    'functionSupport': '1_1',
    'userId': '2850086000373027919',
    'webOfficeEditToken': '28500860003730279191608729092067',
    'logId': '0a89bd9404ac003a-be1adf5c370001f9',
    'HW_refts_hicloudportal_2_cloud_huawei_com': '1608729092794',
    'HW_idvc_hicloudportal_2_cloud_huawei_com': '2',
    'CSRFToken': '0c390f59c1967b9433365510b0bd7741c5fca9144a65e389',
    'JSESSIONID': '3BCFFB2ED9DA2DE27F856A560FA71F92',
}

headers = {
    'Connection': 'keep-alive',
    'x-hw-account-brand-id': '0',
    'CSRFToken': '0c390f59c1967b9433365510b0bd7741c5fca9144a65e389',
    'x-hw-device-manufacturer': 'HUAWEI',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept': 'application/json, text/plain, */*',
    'x-hw-device-brand': 'HUAWEI',
    'Cache-Control': 'no-cache',
    'userId': '2850086000373027919',
    'x-hw-app-brand-id': '1',
    'Origin': 'https://cloud.huawei.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cloud.huawei.com/home',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

data = '{"traceId":"01001_02_1608729094_35193789_101101302_PAR-AL009.1.0.353C00E351R1P1","deviceId":"BC4407EEDD4C68B03C3F886946158389889818DD77C99FEB447124BA89B51F0B","deviceType":9,"perDeviceType":"0","sequence":0,"endpointCrypted":"0"}'
cursor = conn.cursor()
response = requests.post('https://cloud.huawei.com/mobile/queryLocateResult', headers=headers, cookies=cookies, data=data)
dd=json.dumps(response.text)
c=eval(dd)
d=json.loads(c)
info=json.dumps(d['info'])
f=eval(info)
cd=json.loads(f)
lat=cd['latitude']
long=cd['longitude']
xy=str(lat)+","+str(long)
shuju= "http://api.map.baidu.com/geocoder?location="+xy
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# 使用urllib进行网页数据遍历 (json)
url=shuju
vv= urllib.request.urlopen(url, context=ctx).read()
shi=vv.decode("UTF-8")
tree = ET.fromstring(shi)
shuzi=d["currentTime"]
sstr=str(shuzi)[:-3]
sint=int(sstr)
t=timestamp_to_date(sint)
ba=cd["batteryStatus"]
bat=json.loads(ba)
per=str(bat["percentage"])+"%"
pent=int(bat["percentage"])
ischa=bat["isCharging"]
if(ischa=="0"):
    stat="未充电"
else:
    stat="正在充电"
for r in tree.findall(".//formatted_address"):
    loc=r.text
net=cd["networkInfo"]
netw=json.loads(net)
nett=netw["type"]
if(nett=="0"):
    nstat="WIFI"
else:
    nstat="4G"
netn=netw["name"]
sig=int(netw["signal"])
if(sig==0):
    sinal="·"
elif(sig==1):
    sinal="·-"
elif(sig==2):
    sinal="·--"
elif(sig==3):
    sinal="·---"
elif(sig==4):
    sinal="·----"
print("-"*20+t+"-"*20)
print("当前位置:"+str(loc))
print("当前网络:"+nstat)
print("网络信号:"+sinal)
print("电池状态:"+per)
print("充电状态:"+stat)
print("-"*60)
cursor.execute("INSERT INTO mob (timestamp,locat,x,y,ischar,percent,sig,network) VALUES('%s','%s','%s','%s','%s',%d,%d,'%s')" % (t,loc,lat,long,stat,pent,sig,nstat))
conn.commit()

