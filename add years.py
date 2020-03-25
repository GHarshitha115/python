import datetime
def addyears(dt,b):
    try:
        print(dt.replace(year=dt.year+b),end='')
    except ValueError:
        #print(dt+(datetime.date(dt.year+b,1,1)-datetime.date(dt.year,1,1)),end='')
        x=(datetime.date(dt.year+b,1,1))
        y=datetime.date(dt.year,1,1)
        #print(x)
        #print(y)
        print((x-y)+dt,end='')

import datetime 
a=input()
b=int(input())
x=datetime.datetime.strptime(a,'%b %d %Y')
date=x.date()
addyears(date,b)
