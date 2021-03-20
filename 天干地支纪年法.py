# 已知1984是甲子年; 1900-1-1是星期一 。
# 输入以下格式日期"year-month-day"，输出xxxx年为xx年(干支纪年)，
# 输出year-month-day是这一年的第几周,
# year-month-day是这一年的第几天。
# 提示: find(str,i,j) i,j表示搜索的起始和终止位置，包含j
# 甲、乙、丙、丁、戊、己、庚、辛、壬、癸
# 子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥
# 注意判断平年闰年,闰年是366天
# 测试数据：2020-1-1
# 测试数据：2020-1-6  一月六日是第二周

RiQi = input("输入以下格式日期\"year-month-day\":")
Tiangan = ['甲','乙','丙','丁','戊','己','庚','辛','壬','癸']
Dizhi = ['子','丑','寅','卯','辰','巳','午','未','申','酉','戌','亥']
pingnian = [31,28,31,30,31,30,31,31,30,31,30,31]
runnian = [31,29,31,30,31,30,31,31,30,31,30,31]

# 确认年月份
year = int(RiQi[0:4])
temp1 = RiQi.find('-')
temp2 = RiQi.rfind('-')
month = int(RiQi[5:temp2])
day = int(RiQi[temp2+1:])

# 年
i = (year-1984)%10
j = (year-1984)%12
Now = Tiangan[i]+Dizhi[j]

# 日
Day = 0
RunNian = ((year%4==0 and year%100!=0) or year%400==0) #判断是否是闰年
if RunNian:  # 闰年
    for i in runnian[0:month-1]: # 注意索引从0开始，所以month-1
        Day = Day + i
else:   # 平年
    for i in pingnian[0:month-1]:
        Day = Day + i
Day = Day + day

# 周，得先确定那一年的1月1日是星期几，这就用到了一个式子
# 基姆拉尔森计算公式
# 如果temp等于0，是周日；temp等于1，是周一
temp = ((year-1)+(year-1)//4-(year-1)//100+(year-1)//400+1)%7
Week = (Day+temp+5)//7

# 输出
print(RiQi[0:4],"年为",Now,"年")
print(RiQi,"是这一年的第",Week,"周")
print(RiQi,"是这一年的第",Day,"天")
