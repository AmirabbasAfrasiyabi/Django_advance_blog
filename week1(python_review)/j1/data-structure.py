# # list

# # Python lists are mutable
# l = [1, 'abc', True]
# l.append(False)
# print(l)
# l.insert(1,2)
# print(l)
# l2 = l.copy()
# l2[0] = 2
# # l2.extend([5, 12])
# # l2 += [5, 12]
# # print(l)
# print(l2)

# Copy on write
# a = 'Hello'
# b = a 
# b += ', world!'
# print(a)
# print(b)

# stack (LIFO: Last in first out)

# print(l2)
# print(l2.pop(1))
# print(l2)

# queue (FIFO: First in first out)

# q = []
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.pop(0))
# print(q)
# print(q.pop(0))
# print(q)
# print(q.pop(0))
# print(q)

# from collections import deque
# q = deque()
# q.append(1)
# q.append(2)
# q.append(3)
# print(q.popleft())
# print(q.popleft())
# print(q.popleft())

# List Comprehension
# list_variable = [x for x in iterable]
# l = range(100)
# uneven = [x**2 for x in l]
# print(uneven)

# l = [0] * 1000
# print(l)

# matrix = [[0] * 4] * 3
# print(matrix)
# matrix[0][1] = 1
# print(matrix)

# matrix = [[0 for col in range(4)] for row in range(3)]
# matrix[0][1] = 1
# print(matrix)

# slicing

# [1,  2,  3,  5,  7,  9]
#  0   1   2   3   4   5
# -6  -5  -4  -3  -2  -1

# l = [1, 2, 3, 5, 7, 9]
# s1 = l[::]
# l[0] = 6
# print(l)
# print(s1)

# when does a list grow its size?
# https://github.com/python/cpython/blob/main/Objects/listobject.c#L63


# append
# clear
# copy
# count
# extend
# index
# insert
# pop
# remove
# reverse
# [::-1]
# sort

# tuple

# l = [1, 2, 3]
# t = (l,)
# l.append(2)
# print(t)

# dict

# d = {
#     'Ali': '09123456789',
#     'Reza': '09123456782',
# }
# for key in d.keys():
#     print(key)
# for value in d.values():
#     print(value)
# for key, value in d.items():
#     print(key, value)

# if 'Ali' in d:
#     print('Yes')

# del d['Ali']
# print(d['Reza'])

# squares = {x: x * x for x in range(6)}
# print(squares)

# Collision Resolution:
# https://www.scaler.com/topics/data-structures/open-addressing/

# How python dictionaries work (see the "Python dictionaries" section):
# https://tenthousandmeters.com/blog/python-behind-the-scenes-10-how-python-dictionaries-work/

# Open addressing vs. separate chaining:
# https://mathcenter.oxford.emory.edu/site/cs171/collisionResolution/


# ترتیپ دادن به دیکشنری
# collections.OrderedDict
from collections import defaultdict

d = defaultdict(lambda: 0)
print(d[2])

#hash
# 1-  از هش به کی نمیرسه رسید ولی از کی میشه به هش میشود رسید
# 2-hash table->   . یک لیست دارم که یک سری مقادیر دارم . اما اندیس مقادیر بسیار مهم است 
# 3- hash collision -> . وقتی باقیمانده تقسیم بر طول لیست دو نفر یکی شد تداخل پیش می اید و ان موقع به مبحث  میپردازیم  
# 4- روشهای حل این مشکل 
# # https://mathcenter.oxford.emory.edu/site/cs171/collisionResolution/


# set
# مقادیر تکراری را نمیپذیرد از مکانیز م هش کردن استفاده میکند و همه اعضا را مانند لیست جستجو نمسکند که موجود است یا نه و از مکانیزم هش کردن استفاده میکند
# s = {'a', 'e', 'i', 'o', 'u'}
# print(s)
# # ترتیب توش رعایت نمیشه
# s.add('b')
# s.add('b')
# # اعداد تکراری را قبول نمبکند
# print(s)
# s.remove('b')
# print(s)
# s.pop()
# print(s)

# s1 = s
# s2 = {1, 2, 3, 4, 'a', 'b'}

# print(s1 | s2) # union (اچتماع)
# # print(s1 & s2) # intersection( اشتراک)
# # print(s1 - s2) # difference ( تفاضل)
# # print(s1 ^ s2) # symmetric difference ((s1 | s2) - (s1 & s2)) (اجتماع - اشتراک)

# l = [1, 2, 3, 1, 2]
# s = set(l)
# print(s)

# l = [1, 2, 3]
# s = {l}
# print(s) # error

# A bit different from dict when handling collisions (see the "A note on sets" section):
# https://tenthousandmeters.com/blog/python-behind-the-scenes-10-how-python-dictionaries-work/

# priority queue (heap) 
# from queue import PriorityQueue
# customers = PriorityQueue()
# customers.put((2, 'Harry'))
# customers.put((3, 'Charles'))
# customers.put((1, 'Riya'))
# customers.put((4, 'Stacy'))
# while customers:
#      print(customers.get())
