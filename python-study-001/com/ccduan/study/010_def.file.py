

# 函数

def print1():
    print("1")
    return "value"

str = print1()
print(str)

# with的用法
with open("abc.txt",encoding='utf-8') as f:
    print(f.read())

# 可变长参数
print("abd")
print("abc",end="\n")
print("---")

def func(a,*other):
    print(len(a)+len(other))

func("123")
func("123"," 424")

# 函数变量作用域
#
print("*******************")
var1 = 466
def func():
    # 改变作用域，
    global var1
    var1 = 789
    print(var1)
func()
print(var1)

# 迭代器
print("--------------迭代器--------")
list1 = [1,2,3]
it = iter(list1)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))# except


print("-------分割线range----")
#
for i in range(1,10,5):
    print(i)

# 生成器 1到10，步长0.5
print("生成器-------------")
def floatRange(start,stop,step):
    x=start
    while x < stop:
        yield  x #生成器
        #print(x)
        x+=step

for i in floatRange(1,10,0.5):
    print(i)