#条件与循环


# if 条件语句
a =1
if a<0:
    print("a是负数")
    print("这里还是if代码块")

#-----  if  else 结构--------
b="abcd"
if b=="abc":
    print("b 等于 abc")
else:
    print("b不等于abc")
#--------  if elif   else 结构-----------------------

c = int(input("请输入一个数字c："))  #这里相当于强制类型转换
if c>0:
    print("c是正数")
elif c==0:
    print("c不是正数也不是负数")
else:
    print("c是负数")
#----------------------
# 循环语句
#********  for **************
str = "123456789"
for s in str:
    print(s)
#---------------------
print("----------- 分割 线----------")
#-------------------
str1= "123456"

for year in range(2000,2020):
    print("%s   字符串替换测试 %s " %(year,str1) )


#--------   while 循环   -----------

print("-------while 循环----------------")
i=0
while i<10:

    i +=1
    if(i==5):
        #break
        continue
    print(i)