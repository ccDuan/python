# 文件的操作
# 文件内建函数和方法
"""  这是多行注释
open() 打开文件
read() 输入
readline()输入一行
seek()文件内移动
write()输出
close() 关闭文件
"""
# 输出到文件
file1 = open("filetest.txt","w",encoding="utf-8")
file1.write("曹操")
file1.close();
# 读取 输入
file2 = open("filetest.txt","r",encoding="utf-8")
print(file2.read())
file2.close()
# 追加
file3 = open("filetest.txt",'a',encoding='utf-8')
file3.write("刘备")
file3.close()