
#映射的类型： 字典
dict1= {}
print(dict1)
print(type(dict1))

#  字典的操作
dict2={"length":100,"width":10,"length2":200,"width2":20}
#往字典新增 k-v
dict2["length3"]=3
print(dict2)
for key in dict2:
    print(key)
    print(dict2.get(key))