import time

#斐波那契数列：0、1、1、2、3、5、8、13、21、34、……
def fib(n):
    if(n == 1 or n == 2):
        return 1
    return fib(n-1)+fib(n-2)
print(fib(10))

#将一个列表的数据复制到另一个列表中
a = [1,2,5]
b = a[:]
print(b)

#乘法表
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print('%d*%d=%d' % (i,j,i*j),end=' ')
print()

#暂停一秒输出
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print (key, value)
    time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))