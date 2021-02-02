#列表排序及连接
if(__name__ == '__main__'):
    a = [1,3,2]
    b = [3,4,5]
    a.sort()
    print(a)
    #连接列表a与b
    print(a+b)
    print(a,b)
    #连接列表a与b
    a.extend(b)
    print(a)

#循环输出列表
if(__name__ == '__main__'):
    s = ['li','jac','mat','jay','sem']
    for x in range(len(s)):
        print(s[x])

#连接字符串
delimiter = ','
mylist = ['Brazil', 'Russia', 'India', 'China']
print (delimiter.join(mylist))

#列表实用实例
#新建列表  
testList=[10086,'中国移动',[1,2,4,5]]  
#访问列表长度
print(len(testList))
#到列表结尾
print(testList[1:])
#向列表添加元素
testList.append('i\'m new here!')
print(len(testList)) 
print(testList[-1])
#弹出列表的最后一个元素
print(testList.pop(-1))
print(len(testList))  
print(testList)  
#list comprehension
matrix = [[1, 2, 3],  [4, 5, 6],  [7, 8, 9]] 
print(matrix)
print(matrix[1])
#get a  column from a matrix
col2 = [row[1] for row in matrix]
print(col2)
#filter odd item
col2even = [row[1] for row in matrix if row[1] % 2 == 0]
print(col2even)

#列表转换为字典
i = ['a', 'b']
l = [1, 2]
print(dict([i,l]))

#从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止
if __name__ == '__main__':
    from sys import stdout
    filename = input('输入文件名：')
    #创建文件到根目录
    fp = open(filename,'w')
    ch = input('输入字符串')
    while ch != '#':
        fp.write(ch)
        stdout.write(ch)
        ch = input('')
    fp.close()

#从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存
if __name__ == '__main__':
    fp = open('test.txt','w')
    string = input('please input a string:\n')
    string = string.upper()
    fp.write(string)
    fp = open('test.txt','r')
    print(fp.read())
    fp.close()