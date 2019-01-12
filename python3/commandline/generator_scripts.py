#run below in Python command line


# Need change below FULL path
filename = r"C:\Apps\davidyshuang\python3\python3\data\NASDAQ_20101105.csv"
f=open(filename,'r')
it = f.__iter__()
it.__next__()

# use debug, you will see how yield works
def countdown(n):
    print('Counting from ',n)
    while n>0:
        yield n  # Emit a value
        n-=1
    print('Done')

for x in countdown(5):
    print (x)

# demo of using generator in a pipeline
#

def grep ( pattern, infilename):
    with open(infilename,'r') as f:
        for line in f:
            if pattern in line:
                yield line

for line in grep ('VVTV',filename):
    print(line)

nums = [1,2,3,4,5,6]
squares = [ x * x for x in nums ]

nums = [1,2,3,4,5,6]
squares = ( x * x for x in nums )
for x in squares:
    print(x)
sum(squares)   # 由于生成器只能用一次，这里返回值为0

nums = [1,2,3,4,5,6]
squares = ( x * x for x in nums )
sum (squares)