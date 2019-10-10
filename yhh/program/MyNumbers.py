# coding:utf-8
# author:yuhuanhuan
# datetime:2019/10/10 2:46 下午

# StopIteration异常用于标示迭代的完成，防止出现无限循环的情况，在_next_()方法中可以设置在完成指定循环次数后出发StopIteration异常
#来结束迭代

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
myiter = iter(myclass)

for x in myiter:
    print(x)
