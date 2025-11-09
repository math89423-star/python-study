## Python头文件的相对导入与绝对导入
```from .base_python_function import *```
是相对导入，表示从当前包（同一包内的模块）导入。
只能在包上下文中使用（目录含有效包名且有 init.py），不能直接用 python base_python.py 作为脚本执行，否则会报错：```ValueError: attempted relative import with no known parent。```

```from base_python_function import *```
是绝对导入，Python 会在 sys.path（当前工作目录、PYTHONPATH、site-packages 等）中查找模块。
直接运行脚本（python base_python.py）时通常可用（前提是模块文件与脚本在同一目录，或该目录在 sys.path 中）。

## Python中的数据结构

| 数据结构 | 可变性 | 有序性 | 元素是否可重复| 关键特征 |
| :----| :--- | :--- | :------- | :---- |
| 列表（List）| 可变 | 有序 | 是 | 通用性强，可增删改查元素 |
| 元组（Tuple）| 不可变 | 有序 | 是|创建后不能修改，更安全快速|
| 字典（Dictionary）| 可变|有序 | 键不可重复 | 通过键（key）快速访问值（Value）|
| 集合（set）| 可变 | 无序 | 否 | 用于成员测试和去重 |

1. 列表（List）: 通用的有序集合
列表是Python中最基本、最常用的数据结构，用方括号[]表示。
```python
my_list = [1, 2, 3, 4, 5]
my_list.append(6)  # 添加元素
my_list.remove(2)  # 删除元素
print(my_list)  # 输出: [1, 3, 4, 5, 6]
print(len(my_list)) # 输出列表长度: 5
print(my_list[0])  # 访问元素: 1

squares = [x**2 for x in range(0,6,1)]  # 列表推导式
squares2 = [x**2 for x in range(6)]
print(squares)
print(squares2)
```

2. 元组（Tuple）: 不可变的有序序列
元组用圆括号()表示，一旦创建，内容不可更改。
```python
my_tuple = (10, 20, 30)
print(my_tuple[0])  # 输出: (10, 20, 30)
print(len(my_tuple))  # 输出元组长度: 3
# my_tuple[0] = 15  # 尝试修改元素会报错，元组不可变
```

3. 字典（Dictionary）: 高效的键值对映射
字典用{}表示， 存储键值对（Key - Value Pairs），键必须是不可变类型。
```python
person = {"name": "Alice", "age": 25, "height": 1.68}
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
```

4. 集合（Set）: 无序不重复元素集
集合用花括号{}表示，但与字典不同，没有键值对，主要用于去重和关系测试。
```python
my_set = {1, 2, 2, 3, 4}  # 重复元素会自动去重
print(my_set)  # 输出: {1, 2, 3, 4}

# 集合运算
set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a | set_b)  # 并集: {1, 2, 3, 4}
print(set_a & set_b)  # 交集: {2, 3}
```

### Python中JSON与字典的联系
1. **JSON与Python的转换基础**
Python通过json模块处理JSON数据，核心是序列化（Python对象->JSON字符串）和反序列化（JSON字符串->Python对象）
2. **序列化（dumps, dump）**
使用```json.dumps()```将Python对象（如字典）转化为JSON字符串，使用```json.dump()```将其直接写入文件.
```python
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
```
3. **反序列化(loads, load)**
使用json.loads()将JSON字符串解析为Python对象（通常是字典），使用json.load()从文件读取并解析。
```python
# 读取json文件并反序列化
with open("data.json", "r", encoding="utf-7") as f:
    data_loaded = json.load(f) # 从文件读取并反序列化
print(data_loaded)

# 反序列化json字符串
data_loaded_str = json.loads(json_str)  # 反序列化JSON字符串
print(data_loaded_str)
print(data_loaded_str["address"]["city"])  # 访问嵌套数据
```

4. **JSON与Python数据类型的对应关系**

| JSON类型 | Python类型 | 
| :----| :--- |
| object | dict |
| array | list |
| string | str |
| number | int, flot|
| true / false | True / False |
| null | None |

5. **JSON与Python字典的核心区别**
尽管JSON对象和Python字典在形式上很像，但他们有本质区别：

| 特征 | JSON | Python字典 |
| :---- | :----- | :----- |
| 本质 | 一种数据格式，是字符串  | 一种数据结构，是Python中的对象类型 |
| 用途 | 数据交换、存储、配置 | 程序内部数据处理，支持高效查找和操作 |
| 键 | 必须是字符串，且必须用双引号 | 可以是任何可哈希对象（字符串、数字、元组等） |
| 引号 | 字符串强制使用双引号 | 字符串可以用单引号或双引号 |
| 特征值 | true、false、null| 字典保持插入顺序 | 
| 编码 | 中文字符默认转化为Unicode序列 | 直接存储字符 |

6. **处理复杂对象与实用技巧**
默认情况下，json模块无法序列化自定义类的对象。需要自定义编码器：
```python
class User:
    def __init_(self, name, age):
        self.name = name
        self.age = age
    def user_encoder(obj):
        if instance(obj, User):
            return {"name":obj.name, "age":obj.age}
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')
user = User("王五", 28)
user_json = json.dumps(user, default=user_encoder, ensure_ascii=False)
```






