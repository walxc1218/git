a = 1
while a <=100:
    print(a)
    a += 1
    
while语句嵌套
while语句本身是语句
和其他语句一样，可以嵌套到任何的复合语句当中
while 真值表达式１：
    while    

练习：
输入一个数，打印指定的宽度的正方形
输入正方形宽度：５
12345
12345
12345
12345
12345
宽度为　３
123
123
123

#输入一个数，来指定正方形宽度w
w = int(input("请输入正方形的宽度："))
# 打印一行从１到w的数
i =1
while i <= w:
    print(i,end = "")
    i += 1