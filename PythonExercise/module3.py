#递归
def output(s,l):
    if(l==0):
        return
    print(s[l-1])
    output(s,l-1)
s = input('Input a string:')
l = len(s)
output(s,l)

#按相反的顺序输出列表的值
a = ['one', 'two', 'three']
for i in a[::-1]:
    print (i)

#使用函数，输出三次 RUNOOB 字符串
def hello_runoob():
    print ('RUNOOB')
def hello_runoobs():
    for i in range(3):
        hello_runoob()
if __name__ == '__main__':
    hello_runoobs()

#字符串长度
if(__name__ == '__main__'):
    s = input('输入字符串：')
print('长度%d' % len(s))
