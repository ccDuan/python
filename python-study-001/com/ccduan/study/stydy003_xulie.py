#序列  包括字符串，元组 ，列表
#字符串"abc"

week="一二三四五六日"
print(week[0])#下标从0开始

print(week[0:4])# 访问下标为 0 1 2 3的四个

print(week[-1]) #从后往前

print("------------")

a=6
print(week[a%7]) #取余数

#判断6是否在week中
print("三" in week)
# 判断是否不在week中
print("三" not in week)

# 字符串连接操作
print(week + "python好简单")

# 字符串重复操作
print("我爱python"*3)

#*******************元组********************************
#元组存储的内容是不可变更的
yuanzu = ("太阳","月亮","地球")

# 元组嵌套
erwei = (("123",u"湖北"),("456","广东"),("湖南"))

#元组的大小比较
print((1)>(5))
#两个数字的元组大小比较,可以理解为 220>310
print((2,20)>(3,10))

#*******************列表*******************
#列表存储的内容是可以变更的
aList = ["abc","def",1,"ghi"]
#添加元素
aList.append("上海")
print(aList)
#移除元素
aList.remove("abc")
print(aList)