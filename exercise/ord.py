#   1. 写一个程序,输入一个字符串,如果字符串不为空,则把这个字符
#      串的第一个字符的编码打印出来


s = input("请输入一段字符串:")
if s:  # 如果s不为空,则bool(s) 为True
    print("第一个字符的编码值是:", ord(s[0]))
    