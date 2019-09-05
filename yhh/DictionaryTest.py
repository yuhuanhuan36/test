#coding utf-8
# @Time: 2019/9/4 16:38
# @Author: yuhuanhuan
#字典是另一种可变容器模型，且可存储任意类型对象。
#字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中
#键必须是唯一的，但值则不必。
#值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

#访问字典里的值
print("dict['Alice']:", dict['Alice'])

#修改字典
dict2 = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
dict2['Age'] = 8
dict2['school'] = '菜鸟教程'

print(dict2)
#删除字典元素
del dict2['Name']
print(dict2)
dict2.clear()
print(dict2)

'''
字典键的特性
字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
两个重要的点需要记住：
1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
'''
dict3 = {('Name'): 'Runoob', 'Age': 7}

print("dict3('Name'): ", dict3['Name'])

#字典内置函数&方法
'''
    len(dict)   计算字典元素个数，即键的总数。
    str(dict)   输出字典，以可打印的字符串表示。
    type(variable)  返回输入的变量类型，如果变量是字典就返回字典类型。
'''
"""
    radiansdict.clear()     删除字典内所有元素
    radiansdict.copy()      返回一个字典的浅复制
    radiansdict.fromkeys()  创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
    radiansdict.get(key, default=None)  返回指定键的值，如果值不在字典中返回default值
    key in dict     如果键在字典dict里返回true，否则返回false
	radiansdict.items()     以列表返回可遍历的(键, 值) 元组数组
    radiansdict.keys()      返回一个迭代器，可以使用 list() 来转换为列表
    radiansdict.setdefault(key, default=None)和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    radiansdict.update(dict2)   把字典dict2的键/值对更新到dict里
    radiansdict.values()    返回一个迭代器，可以使用 list() 来转换为列表
    pop(key[,default])      删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
	popitem()       随机返回并删除字典中的最后一对键和值。 
"""