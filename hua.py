import json
import urllib.request, urllib.parse, urllib.error
import ssl
import os
from urllib.parse import unquote
import demjson
shuju= "https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish"
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# 使用urllib进行网页数据遍历 (json)
url=shuju
data = urllib.request.urlopen(url, context=ctx).read().decode("UTF-8")
dd=json.dumps(data)
c=eval(dd)
d=json.loads(c)
sc=[]
for u in d["data"]:
    for s in u["trend"]["updateDate"]:
        sc.append(s)
print(sc)
