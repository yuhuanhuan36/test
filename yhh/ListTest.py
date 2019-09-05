# coding utf-8
# @Time: 2019/9/4 14:57
# @Author: yuhuanhuan
list = ['Rita', 'honey', 1989, 2017]
list2 = [1, 2, 6, 3, 5]
list3 = ["a", "b", "c", "d"]
print("list[0]:", list[0])

del list[2]  # 删除列表第三个元素
print("list第三个元素为:", list[2])

# Python列表脚本操作符
print("list2长度为：", len(list2))  # list长度list
print("组合list为：", list2 + list3)  # list组合
print("HI " * 4)  # 重复
print("a" in list3)  # 判断字符串a是否存在list3中

# Python列表截取与拼接
print("打印第三个元素", list2[2])  # 3;打印第三个元素
print("打印倒数第二个", list2[-2])  # 4;打印倒数第二个
print("从第三个开始打印", list2[2:])  # 3,4,5；从第三个开始打印

for a in (list3):  # for循环，迭代
    print(a, end=" xx")


# 嵌套列表


# Python列表函数&方法
print("打印list2的长度", len(list2))
print("打印list2的最大值", max(list2))
print("打印list2的最小值", min(list2))
#list.seq  # 将元组转换为列表


#方法
list.append(2019)#在列表末尾添加新的对象
print("after appent list",list)
print("list count:",list.count('honey'))#统计某个元素在列表中出现的次数

list.copy()#复制列表
print("copy:",list)

list.extend(list2)#在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
print(" after list extend list2",list)
print("list index",list.index('Rita'))#从列表中找出某个值第一个匹配项的索引位置
list.insert(1,'1990')#将对象插入列表
print("inster:",list)
list.pop(-1)#移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print("pop:",list)
list.remove(2019)#移除列表中某个值的第一个匹配项
print("remove:",list)
list.reverse()#反向列表中元素
print("reverse:",list)
list2.sort()#对原列表进行排序
print("sort:",list)
list.clear()#清空列表
print("clear:",list)

