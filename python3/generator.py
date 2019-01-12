
# 迭代 Iteration
for x in [1,2,3,4,5]:
    print(x,end="\n")

names = ['YAHOO','IBM','APPL']
for name in names:
    print(name)

# 生成器函数
def gFunc01():
    print('Start calling gFunc01')
    yield 'IBM'
    print("After returned 'IBM' excutes this line" )
    yield 'YAHOO'
    yield 'APPL'

for x in gFunc01():
    print (x)

# 生成器函数
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

