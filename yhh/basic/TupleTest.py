#coding utf-8
# @Time: 2019/9/4 15:58
# @Author: yuhuanhuan


#Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
#元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

tup1 = ('Rita', 'honey', 1989, 2017)
tup2 = (1, 2, 6, 3, 5)
tup3 = ("a", "b", "c", "d")
print(type(tup3))   #<class 'tuple'>

#创建空元组
tup4 = ()
#元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用

tup5 =(50)
print("type tup5", type(tup5))
tup6 = (50,)
print("type tup6", type(tup6))

#访问元组,元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
print("tup1[2]:", tup1[2])
print("tup2[1:2]:", tup2[1:2])
#修改元组,元组中的元素值是不允许修改的，但我们可以对元组进行连接组合
tup7 = tup1 + tup3
print("tup7:", tup7)
#删除元组
del tup7
#print("tup7:", tup7)

#元组运算符

print("len:", len(tup1))
print("tup2*4:", tup2*4)
print('Rita' in tup1)

#元组索引，截取
print("tup1[2]:", tup1[2])
print("tup1[-2]:", tup1[-2])
print("tup1[2:]", tup1[2:])
#元组内置函数

#len(tuple)#计算元组元素个数。
#max(tuple)#返回元组中元素最大值。
#min(tuple)#返回元组中元素最小值。
#tuple(seq)#将列表转换为元组。

