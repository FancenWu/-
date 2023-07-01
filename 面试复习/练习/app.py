from __future__ import print_function
from math import sqrt
import string

import torch
import numpy as np

'''
x = torch.zeros(5, 3, dtype=torch.long)
y = torch.rand(5, 3)
print(x + y)

result = torch.empty(5, 3)
torch.add(x, y, out=result)
print(result)
y.add_(x)  # 任何一个就地改变张量的操作后面都固定一个 _ 。例如 x.copy_（y）， x.t_（）将更改x
print(x[:, 1])

x = torch.randn(4, 4)
y = x.view(16)
z = x.view(-1, 8)  # the size -1 is inferred from other dimensions
print(x.size(), y.size(), z.size())

a = torch.ones(2, 2, requires_grad=True)
b = a + 2
z = b * b * 3
out = z.mean()
out.backward()
print(a.grad)
'''

'''
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
arr.append(0)

word = "123456"
print(type(word))
num = int(word)
# arr[:] = arr[-k:] + arr[:-k]
print(num)
'''

'''
list1 = [1, 8, 5, 6, 7, 10]
set1 = {1, 2, 3, 4, 5}
set2 = set(range(1, 10))
set3 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
set1.add(10)
set1.update([11, 12])

print(list(set1))
'''


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print("%s is studying %s" % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print("%s only watch cartoon" % self.name)
        else:
            print("%s can watch other movies" % self.name)

student1 = Student("chenfan", 22)
student1.watch_movie()
