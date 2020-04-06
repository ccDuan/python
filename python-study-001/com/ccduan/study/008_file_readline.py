
# 读取一行readline
file4=open("filetest.txt",encoding='utf-8')
print(file4.readline())
file4.close()

# 多行
file5=open("filetest.txt",encoding='utf-8')
for line in file5.readlines():
    print(line)
file5.close()

# 文件中的指针
print("----------")
file6 = open("filetest.txt",encoding='utf-8')
print(file6.tell())
file6.read(2)
print(file6.tell())
# 设置指针回到0
file6.seek(0)
print(file6.tell())
print("当前指针位置%s "%file6.tell())
print("当前读取到的字符%s "%file6.read())
#第一个参数代表偏移位置，第二个表示偏移位置，0表示从文件开头，1表示从当前位置，2从文件结尾
file6.seek(5,0)
file6.close()