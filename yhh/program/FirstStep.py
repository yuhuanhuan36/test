#coding utf-8
# @Time: 2019/9/5 19:46
# @Author: yuhuanhuan
# Fibonacci series: 斐波纳契数列
a, b = 0, 1

while b < 10:
    print('b:', b, end=',')
    #print('a:', a, end=',')
    a, b = b, a + b


i = 256 * 256
print('i:', i)
'''
    关键字end可以用于将结果输出到同一行，或者在输出的末尾添加不同的字符
'''
