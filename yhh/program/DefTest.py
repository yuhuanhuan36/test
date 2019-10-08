# coding:utf-8
# author:yuhuanhuan
# datetime:2019/9/19 8:49 下午
"""
定义一个函数
你可以定义一个由自己想要功能的函数，以下是简单的规则：

函数代码块以 def 关键词开头，后接函数标识符名称和圆括号 ()。
任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
函数内容以冒号起始，并且缩进。
return [表达式] 结束函数，选择性地返回一个值给调用方。不带表达式的return相当于返回 None。
"""

def hello():
    print("Hello Python3.7!")

hello()

"""
函数调用
定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。
这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。
"""

def area(hight, weight):
    return hight * weight

print(area(20, 30))

def printme(str):
    print(str)
    return

printme("这是我自定义的函数！")
printme("再次调用同一函数")

# 参数传递,在 python 中，类型属于对象，变量是没有类型的：
ab = [1, 2, 3]
ab = 'Runboo'

'''
以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 ab 是没有类型，
她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象
'''

"""
可更改(mutable)与不可更改(immutable)对象
在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。

可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

"""
# python 传不可变对象实例
def changeInt( a ):
    a = 10
    print(a)
b = 2
changeInt(b)
print(b)
'''
实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，
按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，
则新生成一个 int 值对象 10，并让 a 指向它。
'''
# 传可变对象实例 ：可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了

def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4])
    print("函数内取值：", mylist)
    return
mylist = [10, 20, 30]

changeme(mylist)
print("函数外取值：", mylist)
# 传入函数的和在末尾添加新内容的对象用的是同一个引用
'''
以下是调用函数时可使用的正式参数类型：
必需参数
关键字参数
默认参数
不定长参数
'''
# 必须参数 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样
def printStr(str):
    print(str)
    return

# printStr()
# TypeError: printStr() missing 1 required positional argument: 'str'


# 关键字参数：关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
def printKeywords(keywords):
    "打印输入的关键字"
    print(keywords)
    return

printKeywords (keywords = "test")

# 以下实例函数参数的使用不需要使用指定顺序：

def printInfo(name, age):
    print("名字:", name)
    print("年龄:", age)
    return

printInfo('yuhuanhuan', 30)
printInfo(age=29, name='Rita')

# 默认参数：
# 调用函数时，如果没有传递参数，则会使用默认参数。以下实例中如果没有传入 age 参数，则使用默认值：
def printDefault(name, age=35):
     "打印任何输入参数"
     print('名字:', name)
     print('年龄:', age)
     return
printDefault(age=50, name="Happy")
print("------------------")
printDefault(name="sad")

# 不定长参数：
# 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，
# 和上述 2 种参数不同，声明时不会命名。基本语法如下：
'''
def functionname([formal_args,] * var_args_tuple):
    "函数文档字符串"
    function_suite
    return [expression]
加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
'''
def printTuple(args, *vartuple):
    "打印任何输入的参数"
    print("输出：")
    print(args)
    print(vartuple)

printTuple(70, 50, 60)
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：
def printEmptyTuple(args1, *vartuple):
    "打印任何输入的参数"
    print(args1)
    for var in vartuple:
        print(var)
    return
printEmptyTuple(10)

printEmptyTuple(70,50,60)

# 还有一种就是参数带两个星号 ,加了两个星号 ** 的参数会以字典的形式导入。
def printDict(args, **varDict):
    "打印任何输出的参数"
    print("输出:")
    print(args)
    print(varDict)
printDict(1, a=2, b=3)
# 匿名函数：
'''
python 使用lambda来创建匿名函数
匿名函数特点如下：
lambda只是一个表达式，函数体比def简单很多
lambda的主体是一个表达式，而不是一个代码块，仅仅能在lambda中封装有限的逻辑进去
lambda函数拥有自己的命名空间，且不能访问自己参数之外或全局命名空间里的参数
虽然lambda函数只能写一行，却不等同于c和C++里的内联函数，后者的目的是调用小函数时不占用栈内存而增加运行效率
'''

sum = lambda arg1, arg2:arg1 + arg2
print(sum(20,30))
# return 语句
'''
return 语句用于退出函数，选择性的调用方法返回一个表达式。不带参数值的return语句返回为none，
'''

def sum(a, b):
    total = a + b
    print('函数内:', total)
    return total
total = sum(2, 9)
print('函数外:', total)

x = True
def printLine(text):
    print(text, ' Runoob')
printLine('Python')