year=int(input("请输入一个年份："))
if ((year%100!=0)and(year%4==0))or(year%400==0):
    print("%d年是闰年"%year)
else:
    print("%d年不是闰年"%year)