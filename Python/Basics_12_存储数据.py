'''
存储数据
'''

import json

# json.dump
# json.dump()写入文件

number = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)

# json.load
# json.load()读出到内存
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
