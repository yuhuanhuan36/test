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
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

'''
创建一个迭代器
把一个类作为一个迭代器使用，需要在类中实现两个方法_iter()_和_next()_
python 的构造函数为_init()_,它会在对象初始化的时候执行
_iter()_返回一个特殊的迭代器对象，这个迭代器对象实现类_next()_方法，并通过StopIteration异常标示迭代的完成
_next()_（Python2里是next()）方法会返回下一个迭代器对象
'''

# 创建一个返回数字的迭代，初始值为1，逐渐递增1
