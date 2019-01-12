
# 迭代 Iteration
for x in range(0,10,2):
    print(x,end="\n")

#Iterating over a List
for x in [1,2,3,4,5]:
    print(x,end="\n")

#Iterating over a List
names = ['YAHOO','IBM','APPL']
for name in names:
    print(name)

#Iterating over a Dictionary
prices = { 'GOOG' : 490.10,
    'AAPL' : 145.23,
    'YHOO' : 21.71 }
for key in prices:
    print(key)

#Iterating over a String
s = "Yow!"
for c in s:
    print(c)
    
# Ietrating over a file
filename01 = r"C:\Apps\davidyshuang\python3\python3\data\NASDAQ_20101105.csv"
with open(filename01,"r") as filehander01:
    for line in filehander01:
        print(line, end='')

#Consuming iterables
# Reductions, sum(s), min(s), max(s)
# list (s), tuple(s),set(s), dict(s)
# Various operatos, item in s
# Many others in library

#Iterating protocol
'''
items = [1,2,3,4,5]
it = iter(items)
it.__next__()

An inside look at the for statement
for x in obj:
    # statements

Underneath the covers
_iter = iter(obj) # Get iterator object
while 1:
    try:
        x = _iter.__next__() # Get next item
    except StopIteration: # No more items
        break
# statements

Any object that supports iter() is said to be "iterable."
refer to website - 
'''

# to support iteration
class countdown(object):
    def __init__(self,start):
        self.start = start
    
    def __iter__(self):
        return countdown_iter(self.start)

class countdown_iter(object):
    def __init__(self, count):
        self.count = count
    def __next__(self):
        if self.count <= 0:
            raise StopIteration
        r = self.count
        self.count -= 1
        return r

for x in countdown(10):
    print(x,end = " ")

# A simple generator - 生成器函数 -1
def countdown2(n):
    while n > 0:
        yield n
        n -= 1
for i in countdown2(5):
    print(i, end=' ')

# 生成器函数 - 2
def gFunc01():
    print('Start calling gFunc01')
    yield 'IBM'
    print("After returned 'IBM' excutes this line" )
    yield 'YAHOO'
    yield 'APPL'

for x in gFunc01():
    print (x)

# 生成器函数 - 3
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fib(6):
    print(n)

# 生成器表达式
# General syntax - (expression for i in s if condition)
nums = [1,2,3,4,5,6]
squares = ( x * x for x in nums )
# print(sum(squares))  
for x in squares:
    print(x)

print(sum(squares))  # 生成器函数只能用一次，此处为0

class Countdown(object):
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n=self.start
        while n >0:
            yield n
            n-=1

c = Countdown(5)

for x in c:
    print(x)

# 类生成器可以重复使用
for x in c:
    print(x)
