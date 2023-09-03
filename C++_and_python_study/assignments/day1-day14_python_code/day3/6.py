year,month,day=eval(input("请输入年月日，以逗号分隔："))
count=0
monthDayCountNomal=[31,28,31,30,31,30,31,31,30,31,30,31]
monthDayCountUnormal=[31,29,31,30,31,30,31,31,30,31,30,31]
if (year%4==0 and year%100!=0) or (year%400==0):
    for i in range(month-1):
        count+=monthDayCountUnormal[i]
else:
    for i in range(month-1):
        count+=monthDayCountNomal[i]
count+=day
print("这是%d年的第%d天"%(year,count))