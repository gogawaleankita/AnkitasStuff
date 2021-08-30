import os
import datetime

def func1(y,m,d,ms,se,da,mi):

    input_date = datetime.date(y, m, d)
    input_date1 = datetime.datetime.combine(input_date, datetime.time(ms, se, da, mi))
    delta = datetime.timedelta(days=3, seconds=2, microseconds=1, minutes=2)
    t = input_date1 - delta
    # print(input_date1, "  ", t)
    # t = input_date1
    day = t.day
    year = t.year
    month = t.month
    minute = t.minute
    second = t.second
    return input_date,input_date1,t,day,year,month,minute,second
def func2(y,m,d,ms,se,da,mi):
    s = datetime.datetime.strptime('Fri Jan 03 10:34:24 2020', '%a %b %d %I:%M:%f %Y')
    # print(s)
    x = datetime.datetime.combine(datetime.date(y, m, d), datetime.time(ms, se, da, mi))
    # print((x))
    q = x.strftime('%a %b %d %I %M: %S %Y')
    # print(q)
    z = datetime.datetime.strptime(q, '%a %b %d %I %M: %S %Y')
    # print(z)
    return x,q,z

if __name__ == "__main__":
    y,m,d,ms,se,da,mi = map(int, input().split())
    inputs=func1(y,m,d,ms,se,da,mi)
    inputs5=func2(y,m,d,ms,se,da,m)
    print(inputs[0])
    print(inputs[1])
    print(inputs[2])
    print(inputs[3])
    print(inputs[4])
    print(inputs[5])
    print(inputs[6])
    print(inputs[7])
    print(inputs5[0])
    print(inputs5[1])
    print(inputs5[2])