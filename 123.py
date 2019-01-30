# # # # l = [1,2,3,4,5]
# # # # print(l[3])
#1111111111
#2222222222222
#33333333333333
# # # l = [3,5]
# # # l[0:] =[1,2,3,4,5,6]
# # # l2 = l
# # # print(l2)

# # # l =int(input("请输入一些正整数"))
# # # while i > 0:
# # #     if i == -1:
# # #     print("程序结束")
# # # else:
# # #    l +=

# # l = list("hello")
# # s = '-'.jion(l)
# # print(s)

# # 列表推导式
# # 列表推导式是用可迭代对象来创建列表的表达式
# # 作用
# # 用简易方法创建列表
# # 语法：
# # [表达式 for 变量 in 可迭代对象]
# # 或[表达式 for 变量 in 可跌] 
# # 生成一个数字1到9的整数平方的列表，即：
# # l = []
# # for x in range(1,10):
# #     l.append(x**2)
# #     print(l)
# #     l = [x**2 for x in range(1,10)]
# #     print(l)


# # l = [x % 2 ==1 for x in range(1,100)]
# # print(l)  

# # 列表推导式的嵌套
# # [表达式1
# #      for 变量1 in 可迭代对象1 if 真值表达式1
# #         for 变量2 in 可迭代对象 if 真值表达式2]

# #  用字符串“ABC”和字符串“123”生成
# #  ['A1','A2','A3']
# # a='ABC'
# # b='123'
# # l =[x + y]
# # [x +y
# #     for x in a if True
# #         for y in b if True]
# # print(l)
# # l = []
# # l = [x**2 for x in range(1,10)]
# # print(l)

# # for x in range(1,100):
# #     if x % 2 ==1:
# #         print(x)






# # # L=[x for x in range(1,10)]
# # # for x in range(1,10):
# # #     print(x)
# # # L=[x for x in range(1,10) if x%2!=0]
# # # for x in range(1,10):
# # #     if x %2!=0:
# # #         print(x)

# # # for x in 'ABC':
# # #     for y in '123':
# # #         s=x+y
        
        
# # # begin = int(input("请输入一个开始的整数"))
# # # end = int(input("请输入一个结束的整数"))

# # # l = [x for x in range(begin,end) if x % 2 ==0]
# # # print(l)       

# # # s = '100,200,300,500,800'
# # # # l= list(s)
# # # # print(l)
# # # t = ()
# # # for x in range(10):
# # #     t += (x**2,)
# # # print(t)
# # # t = ()
# # # for x in range(10):
# # #     t += (x **2,)
# # t = ()    
# # (x**2 for x in range(10))  ?
# # print(t)

# #       str
# # len(x) max() min()   sum() any() all()
# # 可以用于序列中的函数
# # str() list()  tuple()
# # reversed  sorted(x.reverse = false)

# # 字典
# # 什么是字典
# # dict
# # 字典是一种可变的容器 ，可以存储任意类型的数据
# # 字典中的每个数据都是用键key进行索引，而不像序列 字符串列表 可以用蒸

# # 字典是以{}  以冒号 分隔键值对，各键直接用，隔开
# # 字典的构造函数
# # dict()
# # dict(可迭代对象)
# # dict(关键字传参)
# # 关键字传参
# # dict("ab")   ?

# # frozenset(固定集合)
# # 字典的基本操作
# # 字典的键索引
# # 用[]获取字典内的键  对应的值
# # 语法：
# # v = 字典[键]


# # 添加 修改
# # 语法：
# # 字典[键] = 值
# # 说明：
# # 如果键不存在，创建键
# # del 语句
# # 删除字典的键 同时解除与值的绑定关系

# # 字典的成员资格运算
# #  in/ not in
# #  如果存在 返回True 如果不存在返回false
# # 练习
# # 写程序，将如下信息形成一个字典 seasons
# # '键'     '值’
# # 1        '春季有1,2,3月'
# # 2           '夏季有4,5,6月'
# # 3           '秋季有7 8,9月'
# # 4        '冬季有10.11.12月'
# i = int(input('请输入一个数字'))
# seasons ={1:'春季有1,2,3月',2:'夏季有4,5,6月',3:"秋季有7,8,9月",4:'冬季有10,11,12月'}

# if i == 1:
# # print(seasons[1])
# # elif i == 2:
# # print(seasons[2])    
# # elif i == 3:
# # print(seasons[3]) 
# # elif i == 4:
# # print(seasons[4]) 
# # else:
# #     i > 4
# #     print("您输入的不正确")        

# # a =0
# # b =1
# # l =[]
# # while 

# # 1 添加单词
# # 2 删除单词
# # 3 查找单词
# # 4 退出

# # print('1 添加单词')
# # print('2 删除单词')
# # print('3 查找单词')
# # print('4 退出')
# # i = int(input('请输入要操作的编号：'))
# # l = {}
# # if i   break
# #         l += word== 1:
# # while True:
# #     word = input("请输入单词：")
# #     if i == "":
# #     俩  

    
# #                 #执行添加单词
# # elif i == 2:
# #             #执行删除单词
# # elif i == 3:
# #             #执行查找单词
# # elif i == 4：
# #     pass        #执行退出
# # else:
# #     print("您输入错误，请重新输入：")

# i = int(input('请输入一个整数：'))

# while 
#     print()
# else:
#     print("你输入的不正确")    
# def print_even(n):
#     for x in range(0,n):
#         if x % 2 == 0:
#             print(x,end=" ")

# print_even(100)

# def mymax(a,b):
#     if a > b:
#         print(a)
#     else:
#         print(b)
#     return mymax(100,200)

#     def mymax(a,b):
#         zuida = a
#         if a > b
#             print(a)
#             else:
#                 print(b)
#         retur zuida

# 写一个函数myadd(x,y):
# a = int(input("第一个数是："))
# b = int(input("第一个数是："))
# print(a,"+",b,"的和是"，myadd(a,b))

def myadd(x,y):
    return(x + y)


a = int(input("第一个数是："))
b = int(input("第一个数是："))
myadd(a,b)
print(a,"+",b,"的和是",myadd(a,b))


def get_chinese_char_count,此函数实现的功能是给定一个字符串，返回这个字符串中中文字符的个数
def get_chinese_char_count