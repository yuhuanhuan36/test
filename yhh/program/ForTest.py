# coding:utf-8
# author:yuhuanhuan
# datetime:2019/9/19 2:05 下午
# 循环语句练习
a = 1
while a <10:
    if (a % 2 == 0):
        print('偶数:', a)
    else:
        print('基数:', a)
    a += 1
# 在 Python 中没有 do..while 循环

sum = 0
n = 100
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))

# 无限循环
var = 1
while var == 1:
    num = int(input("请输入整数："))
    print("您输入的数为：", num)
print("Good bye!!!")

# while 循环使用 else 语句

