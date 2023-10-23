# 数据持久性模块
import pickle

path = "Text.txt"

myList = [1, 2, 3, "s", "f", "rt", "et", 0, "h", "sdf"]

with open(path, 'wb') as file_object:
    pickle.dump(myList, file_object)

with open(path, "rb") as file_object:
    tempList = pickle.load(file_object)
    print(tempList)
