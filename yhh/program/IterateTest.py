# coding:utf-8
# author:yuhuanhuan
# datetime:2019/10/9 7:09 下午
import sys  # 引入sys模块
'''

迭代是访问集合元素的一种方式，迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，知道所有的元素被访问结束，迭代器只能往前，不能后退、
迭代器有两个基本方法iter()和next()
字符串，列表或元组对象都可用来创建迭代器

'''

list = [1, 2, 3, 4, 5]
it = iter(list) # 创建迭代器对象

#print(next(it))
"--------"
#print(next(it))
# 迭代器对象可以使用常规for语句进行遍历
#for x in it:
#    print(x, end=" ")

# 也可以使用next函数
'''while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

'''
'''
创建一个迭代器
把一个类作为一个迭代器使用，需要在类中实现两个方法_iter()_和_next()_
python 的构造函数为_init()_,它会在对象初始化的时候执行
_iter()_返回一个特殊的迭代器对象，这个迭代器对象实现类_next()_方法，并通过StopIteration异常标示迭代的完成
_next()_（Python2里是next()）方法会返回下一个迭代器对象
'''

# 创建一个返回数字的迭代，初始值为1，逐渐递增1



class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if(self.a < 20):
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = MyNumbers()
print(myclass)
myiter = iter(myclass)
for x in myiter:
    print(x)

'''
在python中，使用了yield的函数被成为生成器
跟普通函数不同的是，生成器是一个返回迭代期的函数，只能用于迭代，简单来说，生成器就是一个迭代器
在调用生成器运行的过程中，每次遇到yield时函数会暂停运行保存当前所有的运行信息，返回yield的值，
并在下一次执行next()方法时从当前位置继续执行
调用一个生成器函数，返回的是一个函数对象

'''

def fibonacci(n):# 生成器函数 斐波那契
    a, b, count = 0, 1, 0
    while True:
        if(count >n):
            return
        yield a
        a, b =b, a+b
        count += 1
f = fibonacci(10)   # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()


