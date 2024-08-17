# Practice using Python Interpretor

# 算术运算
# 1-2
# 4*5
# 7/5 
# 3**2

#检查变量的类型
#type(10)
#type(2.718)
#type("hello")

#变量
x=10
print(x)

x=100
print(x)

y=3.14
 #x*y
#type (x*y)

#列表
a = [0,1,2,3,4]
print(a)
# len(a)

#a[0]
#a[4]
a[4]=99
print(a)
#a[0:2] # 获取索引为0到2（不包括2！）的元素
#a[1:]  # # 获取从索引为1的元素到最后一个元素
#a[:3] #  获取从第一个元素到索引为3（不包括3！）的元素
#a[:-1] # 获取从第一个元素到最后一个元素的前一个元素之间的元素
#a[:-2]  # 获取从第一个元素到最后一个元素的前二个元素之间的元素

#Dictionary

me={'hright':180}
#me['height']


#布尔
# True/False
# refer to hungury.py

hungry = False

# 条件语句
if hungry:
    print("I'm hungry")
else:
    print("I'm not hungry")
    print("I'm sleepy")

# for 循环
for i in [1,2,3]:
    print(i)

# 函数
def hello():
    print("Hello World")

hello()

#带参数的函数
def hello(object):
    print("Hello " + object + " World")

hello("cat")