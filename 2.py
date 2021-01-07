import time
import os
import datetime
import requests
now_time = datetime.datetime.now()
time1_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
print (time1_str)
try:
            
            os.system("python ./1.py")
            os.system("python ./3.py")
except IncompleteRead:
    
    os.system("python ./1.py")
    os.system("python ./3.py")
def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;
second = sleeptime(0,5,0);
while 1==1:
    time.sleep(second);
    now_time = datetime.datetime.now()
    time2_str = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    print (time2_str)
    try:
            
            os.system("python ./1.py")
            os.system("python ./3.py")
    except IncompleteRead:
        
        os.system("python ./1.py")
        os.system("python ./3.py")
