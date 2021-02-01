#练习1
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=k) and (i!=j) and (j!=k):
                print(i,j,k)
    print('range:',i)

#练习2
i = int(input('净利润：'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if(i>arr[idx]):
        r+=(i-arr[idx])*rat[idx]
        print ((i-arr[idx])*rat[idx])
        i=arr[idx]
print (r)

#练习3
year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))
months = (0,31,59,90,120,151,181,212,243,273,304,334)
if(0 < month <=12):
    sum = months[month-1]
else:
    print('data error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print ('it is the %dth day.' % sum)

#练习4
l = []
for i in range(3):
    x = int(input('int:\n'))
    l.append(x)
l.sort()
print(l)