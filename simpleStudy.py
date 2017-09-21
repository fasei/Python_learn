# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 09:28:00 2017

@author: WC
"""

'''
from PIL import Image

im=Image.open('pic/ic_launcher-web.png')

print(im.format,im.mode)
im.thumbnail((200,100))
im.save("111.png",'png')
'''
#from types import MethodType
class Student(object):
   # __slots__=('name','age')#限制类实例的属性，只能这两个

    def __init__(self,name,age):
        self.name=name
        self.age=age
    #补充一些无效的参数
    def __getattr__(self, item):
        if item=="lalala":
            return  0

#打印对象时输出的内容
    def __str__(self) -> str:
        return 'Student%s'%(self.name)
    __repr__=__str__
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,score):
        if not isinstance(score,int):
            raise ValueError("score must be an int!")
        if score<0 or score>100:
            raise ValueError("score must between 0-100!")
        self._score=score
    def toString(self):
        print('name:%s,age:%s' % (self.name,self.age))

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    #如果需要迭代，需要实现__iter__和__next__两个方法
    def __iter__(self):
        return self

    def __getitem__(self, item):
        if isinstance(item,int):
            a,b=1,1
            for x in range(item):
                a,b=b,a+b
            return a
        if isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L




    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>10000:
            raise StopIteration #如果结束，需要返回StopIteration
        return self.a

def lala(self,score):
    self.score=score

bart=Student('wangchao',22)
print(bart)
bart.toString()
bart.score=10
print(bart.score)
print("lalala%d"%bart.lalala)


Student.lalal='aaa'

#迭代对象
for n in Fib():
    print(n)

print(Fib()[:5])

#==============================================================================
# bart.haha='haha'
# print(bart.haha)
# 
# 
# 
# bart.lala=MethodType(lala,bart)
# bart.lala('lala')
# print(bart.score)
#==============================================================================


