#coding utf-8
# @Time: 2019/9/5 15:54
# @Author: yuhuanhuan
#集合

'''
集合（set）是一个无序的不重复元素序列。
可以使用大括号 { } 或者 set() 函数创建集合，
注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
'''
set1 = {'Rita', 'Candy', 'Monica', 'Candy'}

print(set1)     # 这里演示的是去重功能
set1.add('Mario')
print('set1:', set1)
set2 ={'Daniel', 'Cherry', 'Rita'}

print(set1 - set2)   # 集合a中包含而集合b中不包含的元素
print(set1 | set2)  # 集合a或b中包含的所有元素
print(set1 & set2)   # 集合a和b中都包含了的元素
print(set1 ^ set2)     # 不同时包含于a和b的元素
print('Rita' in set1)    # 快速判断元素是否在集合内

#添加元素
set2.add('Mario')
print('set2:', set2)
set2.add('Mario')#将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作
print('set2:', set2)
#还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等
set2.update({'zelda'})
print('set2:', set2)
#移除元素
set2.remove('zelda')
print('set2:', set2)
#此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误
set2.discard('zelda')
#我们也可以设置随机删除集合中的一个元素,多次执行测试结果都不一样。
# 然而在交互模式，pop 是删除集合的第一个元素（排序后的集合的第一个元素）。
set2.pop()
print('set2:', set2)
#计算集合元素个数
print(len(set2))
#判断元素是否在集合中存在
print('Mario' in set2)


'''
集合内置方法完整列表
    add()	为集合添加元素
    clear()	移除集合中的所有元素
    copy()	拷贝一个集合
    difference()	返回多个集合的差集
    difference_update()	移除集合中的元素，该元素在指定的集合也存在。
    discard()	删除集合中指定的元素
    intersection()	返回集合的交集
    intersection_update()	返回集合的交集。
    isdisjoint()	判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
    issubset()	判断指定集合是否为该方法参数集合的子集。
    issuperset()	判断该方法的参数集合是否为指定集合的子集
    pop()	随机移除元素
    remove()	移除指定元素
    symmetric_difference()	返回两个集合中不重复的元素集合。
    symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
    union()	返回两个集合的并集
    update()	给集合添加元素
'''
print('diff:', set1.difference(set2))
print('set1和set2的交集为：', set1.intersection(set2))
print('set1和set2的并集为：', set1.union(set2))

print('两个集合是否包含相同的元素?', set1.isdisjoint(set2))
print('判断set2是否是集合set1的子集？', set2.issubset(set1))
print('返回两个集合中不重复的元素集合', set1.symmetric_difference(set2))
set2.update(['canary'])
print('set2:', set2)

#4、清空集合
set2.clear()
print('set2:', set2)
