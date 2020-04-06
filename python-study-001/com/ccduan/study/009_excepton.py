
a="123"
#print(a[3])

# try:
#     year = int(input("输入年份 "))
# except ValueError :
#     print("请输入数字")


# 自定义异常
# try:
#     raise NameError("自定义异常")
# except NameError:
#     print("自定义异常2222")

try:
    a= open("bucunzai.txt")
except Exception as e:
    print(e)
finally:
    #关闭
    a.close()