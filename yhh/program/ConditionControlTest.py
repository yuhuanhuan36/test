#coding utf-8
# @Time: 2019/9/5 19:55
# @Author: yuhuanhuan
#条件控制练习
a = 1
while a <10:
    if (a % 2 == 0):
        print('偶数:', a)
    else:
        print('基数:', a)
    a += 1

var1 = 100
if var1:
    print('1 - if 条件表达式为true')
    print(var1)
var2 = 3
if var2:
    print('2-if条件表达式为true')
    print(var2)
print('Good bye!!!')

age = int(input("请输入狗狗的年龄："))
if age == 0:
    print("just kidding!!!")
elif age == 1:
    print("狗狗的年龄相当于人类的14岁")
elif age == 2:
    print("狗狗的年龄相当于人类的22")
elif age > 2:
    human = 22 + (age-2)*5
    print("对应人类的年龄是：", human)


print("点击 Enter键退出！！！")

'''
<	小于
<=	小于或等于
>	大于
>=	大于或等于
==	等于，比较两个值是否相等
!=	不等于
'''

print(5 == 6)

x = 5
y = 8
print(x == y)


# next example
number = 7
guess = -1
print("数字猜谜游戏")
while guess != number:
    guess = int(input("请输入您猜的数字："))
    if guess == number:
        print("恭喜您猜对了！")
    elif guess > number:
        print("不好意思，您猜大了")
    elif guess < number:
        print("不好意思，您猜小了")


num = int(input("请输入数字"))
if num % 2 == 0:
    if num % 3 == 0:
        print("您输入的整数可以被2整除，也可以被3整除")
    else:
        print("您输入的整数可以被2整除，不可以被3整除")

else:
    if num % 3 == 0:
        print("您输入的整数不可以被2整除，但可以被3整除")
    else:
        print("您输入的整数不可以被2整除，也不可以被3整除")