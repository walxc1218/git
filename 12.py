
#输出一个矩形
# print("*********")
# print("         ")
# print("*       *")
# print("         ")
# print("*       *")
# print("         ")
# print("*********")


# print("矩形的周长是：",(6+4)*2,"cm","矩形的面积是：",6 * 4,"cm")

#g = int(input("请输入要计算费用的公里数："))
#if g <= 3:
 #   print("13元")
#elif 3 < g <= 15:
 #   p = 2.3 * g
 #   print(p , "元")
#else:
 #   g >15
    # p = (2.3 * 15) + 3.45 * (g - 15)
    # print(p , "元")      
    
#2
x = int(input("请输入第一个数："))
y = int(input("请输入第二个数："))
z = int(input("请输入第三个数："))
if x > y and x > z:
    print("最大的数是：",x)
if y > x and y > z:
    print("最大的数是：",y)   
if z> y and z > x:
    print("最大的数是：",z)
if x < y and x < z:
     print("最小的数是：",x)
if y< x and y < z:
     print("最小的数是：",y)   
if z < y and z< x:
     print("最小的数是：",z)
h  = (x + y + z)//3
print("三个数的平均数是：",h)




# sg = float(input("请输入身高："))
# tz = float(input("请输入体重："))
# BMI = tz / sg ** 2
# print(BIM)
# if BIM < 18.5:
    # print("体重过轻")
# if 18.5 <= BIM < 24:
    # print("正常范围")
# else:
    # BIM >= 24:
    # print("体重过重")       








