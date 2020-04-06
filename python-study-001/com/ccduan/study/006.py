# 列表推导式 与字典推导式

# 列表推导式
# 计算 1到10所有偶数的平方
alist = []
for i in range(1,11):
    if(i%2==0):
        alist.append(i*i)
print(alist)
# 上面的写法用列表推导式
blist = [i*i for i in range(1,11) if(i % 2) == 0]
print(blist)


# 字典推导式
#z_num ={}
#for i in