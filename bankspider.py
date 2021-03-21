import os
import platform
import sys
import pymysql
conn = pymysql.connect( # 创建数据库连接
    host='localhost', # 要连接的数据库所在主机ip
    user='root', # 数据库登录用户名
    password='#', # 登录用户密码
   database='life', # 连接的数据库名，也可以后续通过cursor.execture('user test_db')指定
    charset='utf8mb4' # 编码，注意不能写成utf-8
)
cursor = conn.cursor()
def function1(a):
    uipath = str(a)
    f=open(uipath, "r",encoding='EUC_KR')
    s = [i[:-1].split('|') for i in f.readlines()[1:]]
    a=0
    for i in s:
        time=i[1][0:10].replace('.','-')
        cate=i[2]
        cont=i[3]
        wi=int(i[4].replace(',',''))
        de=int(i[5].replace(',',''))
        re=int(i[6].replace(',',''))
        print(time+'   '+cate+'   '+cont+'   '+str(wi)+'   '+str(de)+'   '+str(re))
        cursor.execute("INSERT INTO krlife (time,cate,content,withd,dep,odd) VALUES('%s','%s','%s',%d,%d,%d)" % (time,cate,cont,wi,de,re))
        conn.commit()


b=0
path = os.getcwd()
a=os.listdir(path)
for i in a:
    b+=1
    print(str(b)+":"+i)
c=int(input("请输入所要转换文字的幻灯片文件序号:"))
d=c-1
if(platform.system()=='Windows'):
    print('Windows系统')
    e=path+"\\"+a[d] #windows
    print(e)
    function1(e)
if(platform.system()=='Darwin'):
    print('Mac系统')
    e=a[d] #mac
    print(e)
    function1(e)
cursor.close()

