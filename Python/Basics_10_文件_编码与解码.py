path = "Text.txt"

# 编码与解码的格式必须一样

# "b" 表示以二进制的方式写入文件
# .encode("utf-8") 以utf-8格式编码
with open(path, "ab") as file_object:
    str = "这是测试写入内容\n"
    file_object.write(str.encode("utf-8"))

# "b" 以二进制的方式读取文件
# .decode("utf-8") 以utf-8格式解码
with open(path, "rb") as file_object:
    # print(file_object.read())
    print(file_object.read().decode("utf-8"))
