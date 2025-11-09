from base_python_function import grade_calculation
# python是动态类型语言，无需声明类型，直接赋值即可

## 变量与数据类型
name = "Alice"
age = 25
height = 1.68
is_student = True
##  type()函数可与用于查看变量类型
""" 
print(type(is_student))
print(type(name))
print(type(age)) 
"""


## 控制结构
## 控制结构决定了程序的执行流程
## · 条件判断语句if elif else
score = 85
# print(grade_calculation(score))



## 循环结构
### for遍历循环
fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)

### 列表（List）
""" my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # 添加元素
my_list.remove(2)  # 删除元素
print(my_list)  # 输出: [1, 3, 4, 5, 6]
print(len(my_list)) # 输出列表长度: 5
print(my_list[0])  # 访问元素: 1

squares = [x**2 for x in range(0,6,1)]  # 列表推导式
squares2 = [x**2 for x in range(6)]
print(squares)
print(squares2) """


### 元组（Tuple）
""" my_tuple = (10, 20, 30)
print(my_tuple[0])  # 输出: (10, 20, 30)
print(len(my_tuple))  # 输出元组长度: 3
# my_tuple[0] = 15  # 尝试修改元素会报错，元组不可变 """


### 字典（Dictionary）
""" person = {"name": "Alice", "age": 25, "height": 1.68}
print(person)
print(person["name"])  # 访问元素: Alice
person["age"] = 26  # 修改元素
person["city"] = "London"  # 添加新元素
print(person)
print(len(person))  # 输出字典长度: 4
print("name" in person)  # 检查键是否存在: True
for key, value in person.items():  # 遍历字典
    print(f"{key}: {value}")

squres_dict = {x : x**2 for x in range(6)}  # 字典推导式
print(squres_dict)
 """

### 集合（Set）
""" my_set = {1, 2, 2, 3, 4}  # 重复元素会自动去重
print(my_set)  # 输出: {1, 2, 3, 4}

# 集合运算
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a | set_b)  # 并集: {1, 2, 3, 4}
print(set_a & set_b)  # 交集: {2, 3} """


import json
data = {
    "name": "Alice",
    "age": 25,
    "is_student": True,
    "courses": ["Math", "Science"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}
print(data)
# 转化为json字符串
json_str = json.dumps(data, ensure_ascii=False, indent=2)  # 序列化为JSON字符串
# 写入json文件
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)  # 序列化并写入文件

# 读取json文件并反序列化
with open("data.json", "r", encoding="utf-7") as f:
    data_loaded = json.load(f) # 从文件读取并反序列化
print(data_loaded)

# 反序列化json字符串
data_loaded_str = json.loads(json_str)  # 反序列化JSON字符串
print(data_loaded_str)
print(data_loaded_str["address"]["city"])  # 访问嵌套数据