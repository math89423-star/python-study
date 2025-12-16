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

## Python面向对象详解
### 基础概念
| 核心要素 | 说明与要点 |
| :----- | :------ |
| 类（Class） | 对象的蓝图（模板），使用class关键字定义 | 
| 对象（Object） | 类的具体实例，通过类名（）创建 |
| 构造方法 \_\_init\_\_ |  对对象初始化时自动调用的特殊方法 |


1. \_\_init\_\_魔术方法
当类中写了这个方法的时候，第一个参数必须是self，代表当前对象，然后第二个参数开始就随意，但是这些参数在创建对象的时候必须一一实现。
创建对象的时候自动调用\_\_init\_\_方法。
```python
class Person():
    num = 0
    def __init__(self):
        Person.num += 1
print(Person.num) # 实例未创建，不会调用__init__方法，num仍为0
Person()
Person()
Person()
Person()
print(Person.num) # 创建了4个实例，调用了4次__init__方法，num变为4
```
```__init__```：
1.用来构造初始化函数，用来给对象进行初始化属性，所以不需要返回值
2.创建对象的时候自动调用
3.自定义类如果不定义的话，默认调用父类object的，同理继承也是，子类若无，调用父类的，若有，调用自己的。
```python
class Animal:
    def __init__(self):
        #print("init初始化方法，没有调用父类object")
        pass
    
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self):
        super().__init__()  # 调用父类的__init__方法
        #print("Dog的init初始化方法")

    def speak(self):
        super().speak()  # 调用父类的speak方法

Dog().speak()  # 输出: Animal speaks
```
2. 定义类和创建对象

**定义类**
在python中，使用class关键字来定义类。最简单的类：
```python
class Person(object):
    pass
```
**创建对象**
使用类名加括号即可创建对象。例如：
```python
person1 = Person()  # 创建一个Person类的实例
person2 = Person()  # 创建另一个实例
```
3. 类的属性和方法

**属性**
属性是类中定义的数据。可以是类属性（共享）或实例属性（独立）。
```python
class Person(object):
    species = "Homo sapiens"  # 类属性

    def __init__(self, name, age):
        self.name = name  # 实例属性
        self.age = age    # 实例属性
```
**方法**
方法是类中定义的函数，用于描述对象的行为。
特殊方法```__init__```用于初始化对象的实例属性。
```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
```
使用类的属性和方法：
```python
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 访问实例属性
print(person1.name)  # 输出：Alice
print(person2.age)   # 输出：25

# 调用实例方法
print(person1.greet())  # 输出：Hello, my name is Alice and I am 30 years old.
```
4. 类的高级功能
类属性和实例属性的区别
```python
class Test:
    class_attr = "I am a class attribute"

    def __init__(self):
        self.instance_attr = "I am an instance attribute"

# 类属性可以通过类或实例访问
print(Test.class_attr)  # I am a class attribute
obj = Test()
print(obj.class_attr)   # I am a class attribute

# 实例属性只能通过实例访问
print(obj.instance_attr)  # I am an instance attribute
```

## Python类型提示与类型注解
参数类型注解：函数参数中的冒号如```first_name: str```是参数的类型注解，提示参数应为字符串类型
返回值类型注解：如函数后的``-> str``是返回值的类型注解，返回值类型注解是一个可选类型提示，不影响程序实际运行，但是能够提升效率和维护代码。
示例：
```python
def get_full_name(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name

full_name = get_full_name("jone", "doe")
print(full_name)
```
示例2：
```python
def get_name_with_age(name: str, age: int) -> str:
    name_with_age = name.title() + ", age:" + str(age)
    return name_with_age

name_with_age = get_name_with_age("alice", 30)
print(name_with_age)
```
示例3：
```python
from typing import List, Dict
def process_names(names: List[str]) -> List[str]:
    processed = [name.title() for name in names]
    return processed

names = ["alice", "bob", "charlie"]
processed_names = process_names(names)
print(processed_names)  # 输出：['Alice', 'Bob', 'Charlie']

def process_person_info(person_info: Dict[str, int]) -> None:
    for name, age in person_info.items():
        print(f"{name.title()} is {age} years old.")
    return

person_info = {"alice": 30, "bob": 25}
process_person_info(person_info)
```
Python的标准数据类型：
| 数据类型分类 | 具体类型 | 可变性 | 主要特征与用途 |
| :---------- | :------ | :------ | :----------- |
| 数值类型 | 整型（int）、浮点型（float）、复数（complex）、布尔型（bool）| 不可变 | 用于科学计算和逻辑判断，bool是int的子类，值为True(1)或False(0) |
| 序列类型| 字符串（str）、列表（list）、元组（tuple）、范围（range）|字符串、元组、范围不可变，列表可变 | 有序的元素集合。字符串用于文本；列表通用、灵活；元组不可变，常用于保障数据安全|
| 映射类型 | 字典（dict）| 可变 | 通过键值对存储和访问数据，键必须是不可变类型 |
| 集合类型 | 集合（set），不可变集合（frozenset）|集合可变，不可变集合不可变 | 存储无序，不重复的元素，常用于去重和关系测试（如交集，并集）|
| 其他类型 | 空类型（NoneType）、二进制类型（bytes）| None和bytes不可变 | None代表空值；二进制类型用于处理字节数据 | 

可变与不可变的关键区别：是Python中非常重要的概念。
**不可变类型**（如整型，浮点型，字符串，元组）一旦被创建，其内容无法修改，对它的赋值或拼接通常会返回一个权限的对象。
**可变类型**（如列表，字典，集合）内容可以修改，比如向列表追加元素，对象本身的内存地址不会改变。

类型检查函数：
```type()``` 或 ```isinstance()```
```python
# type()函数返回一个对象的类型
num = 42
print(type(num)) # 输出：<class 'int'>

# isinstance()函数，用于判断一个对象是否属于某个类型或子类时
is_string = isinstance("hello", str)
print(is_string) # 输出：True

```

内存地址检查：
获取内存地址：```id()```函数 
```python
name = "Lee"
print(id(name))
```
判断内存一致性：```is```语句
```python
a = "hello"
b = "hello"
print(a is b) # 输出：True，因为字符串是不可变类型，Python会优化内存使用，指向同一对象
a = a + "boy"
print(a is b) # 输出：False，因为字符串拼接后，a指向了一个新的对象


# 判断字符串内容是否相同，应该使用"=="
str1 = "hello"
str2 = "he"
str3 = "llo"
str4 = str2 + str3
print(str1 is str4) # 输出：False，因为str4是通过拼接生成的新对象
print(str1 == str4) # 输出：True，因为内容相同
```

## Python列表切片
在 Python 的列表切片操作 items[int1 : int2] 中，int1 和 int2 用于指定一个前闭后开的索引区间，用来获取列表的一部分。
| 参数 | 含义 | 默认值 | 关键规则 | 
| :---- | :---- | :----- | :-----|
| int1 | 切片开始的索引位置 | 0（列表开头） | 结果包含该索引处的元素 |
| int2 | 切片结束额索引位置 | 列表长度（列表末尾） | 结果不包含该索引处的元素 |

列表切片的通用语法是 ```list[start:end:step]```，其中 step 是步长（可选，默认为1）
对于列表 items = [10, 20, 30, 40, 50]，切片 items[1:4] 获取的是索引 1（元素20）到索引 3（元素40）的元素，因为索引 4 对应的元素50不被包含在内，所以结果是 [20, 30, 40]

Python 列表的索引支持以下几种方式
| 索引类型 | 说明 | 示例（列表 items = [10, 20, 30, 40, 50]）|
| :------- | :---- | :------------------------------------- |
| 正向索引 | 从左侧开始，从0开始计数 | items[1:3] 返回[20, 30] |
| 负向索引 | 从右侧开始，-1表示最后一个元素 | items[-4:-1] 返回 [20, 30, 40] （因为 -4 对应20，-1 对应50但不包含）|
| 省略索引 | 省略int1 表示从头开始；省略int2表示到末尾结束 | items[:3]返回[10, 20, 30]; items[2:]返回[30, 40, 50]; items[:]返回整个列表的浅拷贝|

## Python深拷贝与浅拷贝
在Python中，理解深拷贝与浅拷贝的差异，关键在于理清数据复制的深度以及新旧对象之间的独立性。
| 特性 | 浅拷贝（Shallow Copy）| 深拷贝（Deep Copy）|
|:-----| :------------------- | :----------------- |
| 复制深度 | 仅复制对象的顶层（父对象）| 递归复制对象的所有层级，包括父对象及其所有的子对象 |
| 子对象处理 |  子对象是引用（内存地址相同），新旧对象共享子对象| 子对象是全新对象（内存地址不同），新旧对象的子对象完全独立 | 
| 独立性 | 修改共享的子对象会相互影响 | 修改任一对象的任何部分都不会影响另一个对象 |
| 内存与性能 | 占用内存较少，速度较快 | 占用内存较多，速度较慢 | 
| 适用场景 | 对象结构简单，允许共享子对象 | 需要对象完全独立，或对象有复杂的嵌套 | 

**实现方式与代码示例：**
**浅拷贝的实现**
1. 使用copy模块的copy()函数
2. 使用数据类型自带的copy()方法（适用于列表，字典）
3. 使用切片操作（主要针对于序列类型），例如```list_copy = original_list[:]```
```python
import copy

original_list = [1, 2, ["a", "b"]]
# 方法1 使用copy.copy()进行浅拷贝
shallow_copied_list1 = copy.copy(original_list)

# 方法2 使用list()函数进行浅拷贝
shallow_copied_list2 = original_list.copy()

# 方法3 使用切片进行浅拷贝
shallow_copied_list3 = original_list[:]

# 修改原始列表中的嵌套列表
original_list[2][0] = "changed"

# 打印结果，观察浅拷贝的影响
print("Original List:", original_list)
print("Shallow Copied List 1:", shallow_copied_list1)
print("Shallow Copied List 2:", shallow_copied_list2)
print("Shallow Copied List 3:", shallow_copied_list3)

# 输出结果：
# Original List: [1, 2, ['changed', 'b']]
# Shallow Copied List 1: [1, 2, ['changed', 'b']]
# Shallow Copied List 2: [1, 2, ['changed', 'b']]
# Shallow Copied List 3: [1, 2, ['changed', 'b']]

```
可以看到，修改原始列表中的子对象（内部列表）后，所有浅拷贝得到的列表中的对应子对象也都跟着改变了，因为它们引用的是同一个子列表。但是，如果修改的是顶层元素（例如 original_list[0] = 100），则不会影响浅拷贝对象。

```python
import copy

original_list = [1, 2, ["a", "b"]]
# 方法1 使用copy.copy()进行浅拷贝
shallow_copied_list1 = copy.copy(original_list)

# 方法2 使用list()函数进行浅拷贝
shallow_copied_list2 = original_list.copy()

# 方法3 使用切片进行浅拷贝
shallow_copied_list3 = original_list[:]

# 修改原始列表中的嵌套列表
original_list[0] = 100

# 打印结果，观察浅拷贝的影响
print("Original List:", original_list)
print("Shallow Copied List 1:", shallow_copied_list1)
print("Shallow Copied List 2:", shallow_copied_list2)
print("Shallow Copied List 3:", shallow_copied_list3)

# 输出结果
# Original List: [100, 2, ['a', 'b']]
# Shallow Copied List 1: [1, 2, ['a', 'b']]
# Shallow Copied List 2: [1, 2, ['a', 'b']]
# Shallow Copied List 3: [1, 2, ['a', 'b']]
```
**深拷贝的实现**
深拷贝通常通过copy模块的deepcopy()函数来实现
```python
import copy

original_list = [1, 2, ["a", "b"]]

# 使用copy.deepcopy()进行深拷贝
deep_copied_list = copy.deepcopy(original_list)

# 修改原始列表中的嵌套列表
original_list[2][0] = "change"

# 打印结果，观察深拷贝的影响
print("Original List:", original_list)
print("Deep Copied List:", deep_copied_list)

# 输出结果
# Original List: [1, 2, ['change', 'b']]
# Deep Copied List: [1, 2, ['a', 'b']]
```
在这个例子中，无论修改原始列表的顶层元素还是子对象，深拷贝得到的列表都完全不受影响，因为二者以及它们内部的所有元素都是独立的。选择浅拷贝还是深拷贝，取决于需求：**​是否需要新旧对象在子对象层面也完全独立。**


## Python的逻辑运算符
Python中的逻辑运算只要包括“与”（AND） 或（“OR”） 非（“NOT”）以及 异或（“XOR”）
1. 与（AND）运算
只有当两个操作数都为True时，结果才为True
当第一个操作数为False，则不会计算第二个操作数
2. 或（OR）运算
只要有一个操作数为True，结果就为True
如果第一个操作数为True，则不会计算第二个操作数
3. 非（NOT）运算
对操作数取反，如果操作数为True，则返回False。如果操作数为False，则返回True
4. 异或（XOR）运算
当两个操作数不同时返回True，当两个操作数相同时返回False。
异或可以用（!=）表示

示例：
```python
a = True
b = False
c = True
print(a and b)  # 输出: False
print(a or c)   # 输出: True
print(not b)    # 输出: True

# 异或
# 在Python中没有直接的异或运算符，但可以通过组合使用and、or和not来实现。
# 异或的含义：两个操作数相同则返回False，不同则返回True。
# 使用不等运算符!=，因为布尔值的异或实际上就是判断两个布尔值是否不同。
result2 = a != b
print(result1, result2)  # 输出 True True
```
**位运算符**
位运算符通常用于整数，而逻辑运算符用于布尔值。不过，在Python中，逻辑运算符（and、or、not）可以用于任何类型的对象，因为Python会将它们解释为布尔值（通过调用对象的__bool__方法或__len__方法等）。而位运算符通常用于整数，如果用于其他类型可能会出错。
```python
a = 5  # 二进制 0101
b = 3  # 二进制 0011

print(a & b)  # 按位与：0001，输出1
print(a | b)  # 按位或：0111，输出7
print(a ^ b)  # 按位异或：0110，输出6
print(~a)     # 按位取反：1010（补码表示，取决于整数位数），输出-6

# 公式 ~x = -x - 1 (~5 = -5 - 1 = -6)
```

## Python并发 async / await
Python的现代版本支持通过一种叫做“协程” --使用```async```和```await```语法的东西来写“异步代码”。
**异步**：当程序运行至某个点，不得不停下，等待其他程序运行结束后，再开始往下运行，例如：
```
· 通过网络发送来自客户端的数据
· 客户端接收来自网络中的数据
· 磁盘中要由系统读取并提供给程序的文件的内容
· 程序提供给系统的要写入磁盘的内容
· 一个 API 的远程调用
· 一个数据库操作，直到完成
· 一个数据库查询，直到返回结果
```
这个执行的时间大多是在等待 I/O 操作，因此它们被叫做 "I/O 密集型" 操作。

**同步**：对于"同步"（与"异步"相反），他们通常也使用"顺序"一词，因为计算机程序在切换到另一个任务之前是按顺序执行所有步骤，即使这些步骤涉及到等待

最简单的异步程序：
```python
import asyncio
async def task1() -> None:
    print("Task 1: Starting")
    await asyncio.sleep(2)
    print("Task 1: Completed")
    return

async def task2() -> None:
    print("Task 2: Starting")
    await asyncio.sleep(1)
    print("Task 2: Completed")
    return

async def main() -> None:
    await asyncio.gather(task1(), task2())
    return

if __name__ == "__main__":
    asyncio.run(main())
```

异步编程的真正威力在于并发执行多个任务，大幅提升I/O密集型应用的效率。
```python
import asyncio

async def download_page(url, delay):
    print(f"开始下载 {url}")
    await asyncio.sleep(delay)  # 模拟网络请求
    print(f"完成下载 {url}")
    return f"{url}的内容"

async def main():
    # 同时启动三个下载任务
    results = await asyncio.gather(
        download_page("https://example.com/page1", 2),
        download_page("https://example.com/page2", 1),
        download_page("https://example.com/page3", 3)
    )
    
    print("所有页面下载完成:")
    for result in results:
        print(f"获取到: {result}")

asyncio.run(main())
```

## Python正则表达式
正则表达式是处理文本匹配和查抄的强大工具，尤其适合进行复杂的字符串搜索、替换和验证。
| 模块 | 主要功能 | 
| :---- | :------ |
| re模块 | Python内置的正则表达式模块，提供一系列函数来处理字符串 |
| 正则表达式函数 | 如match()、search()、findall()、sub()、split()等，用于执行不同的任务和操作 |
| 正则表达式对象 | 通过re.compile()预编译正则表达式模式生成的对象，可重复使用以提高效率 |
| 匹配对象 | 成功匹配后返回的对象 | 

**核心函数**
| 函数 | 作用 | 搜索范围 | 返回值 | 适用场景 |
| :---- | :---- | :----- | :----- | :------ |
| re.match(pattern, string) | 从字符串开头匹配模式 | 仅开头 | 第一个匹配的Match对象，否则返回None | 验证字符串是否以特定模式开头（验证URL协议）
| re.search(pattern, string) | 在字符串中搜索第一个匹配项 | 整个字符串 | 第一个匹配的Match对象，否则返回None | 查找字符串中是否存在某个模式（日志查错）|
| re.findall(pattern, string) | 查找所有匹配项 | 整个字符串 | 所有匹配字符串的列表，否则空列表 | 提取字符串中所有符合模式的内容（提取邮箱地址） |
| re.finditer(pattern, string) | 查找所有匹配项 | 整个字符串 | 一个包含所有匹配Match对象的迭代器 | 需获取每个匹配项详细位置时（性能优于findall）|
| re.fullmatch(pattern, string) | 检查整个字符串是否完全匹配模式 | 整个字符串 | 匹配的Match对象（若整个字符串匹配模式）| 严格验证字符串格式（如身份证号、手机号校验）|

示例：
```python
import re
text = "我有3个苹果，5个橙子"
pattern = re.compile(r'\d+')
matches = pattern.findall(text)
print(matches)  # 输出: ['3', '5']
```

**替换与分割字符串**
```re.sub(pattern, repl, string)```:用于替换字符串中的匹配项。repl可以是字符串或一个可以调用的对象。示例：
```python
import re
text = "today is 2024-06-15"
new_text = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', text)
print(new_text)  # 输出: today is 15/06/2024
```

```re.split(pattern, string)```:使用正则表达式模式作为分隔符来分割字符串，示例：
```python
import re
text = "苹果，香蕉，西瓜，橙子，橘子"
fruits = re.split(r'，', text)
print(fruits)  # 输出: ['苹果', '香蕉', '西瓜', '橙子', '橘子']
```
**正则匹配核心符号及作用**
| 符号 | 名称 | 主要作用 | 示例 | 匹配结果 |
| :---- | :---- | :----|:-----|:--------|
| ^ | 脱字符 | 1. 匹配开头：匹配字符串（或多行模式下的行）的开始位置。<br>2. 表示否定：在字符组[]内作为第一个字符时，表示排除该字符组中的字符 | ^The <br> [^0-9] | "The car"中的The <br> 匹配非数字字符，如"a" |
| $ | 美元符 | 匹配字符串（或多行模式下的行）的结束位置。| end$ | "The end"中的"end" |
| . | 点号 | 匹配除换行符外的任意一个单个字符或子表达式 | a.c | "abc","axc" |
| * | 星号 | 匹配前面的单个字符或子表达式零次或多次 | ab*c | "ac","abc","abbc"| 
| + | 加号 | 匹配前面的单个字符或子表达式一次或多次 | ab+c | "abc","abbc" ("ac"无法匹配到)|
| ? | 问号 | 匹配前面的单个字符或子表达式零次或多次 | ab?c | "ac","abc"|
| \ | 反斜杠 | 1. 转义特殊字符，十七失去特殊意义 <br> 2.赋予普通普通字符特殊意义。如\d代表数字 | \\. <br> \d | \\.代表匹配字面的点号"." <br>  \d代表匹配任意数字 | 
| \| | 竖线 | 表示或，匹配它左边或右边的表达式 | cat \| dog | "cat"或"dog" |
| () | 括号 | 1. 分组：将多个元素组合成一个整体 <br> 2. 捕获：提取匹配内容以备以后用 | (ab)+ <br> (\d{3}) | (ab)+可以捕获"ababab" <br> (\d{3})可以捕获三位数字如"123" |


示例：
```python
import re
text = "asadawcbrdfawasdwdsfdafec"
pattern = re.compile(r'as*d')
matches = pattern.findall(text)
print(matches)  # 输出: ['ad', 'asd']

# 理解正则表达式模式 as*d：
# a：匹配字母 'a'
# s*：匹配零个或多个字母 's'（因为 * 表示前面的字符 's' 可以出现0次或多次）
# d：匹配字母 'd'
```
匹配字符串开头：
```python
import re
pattern = r"^Hello"
print(re.search(pattern, "Hello world!")) # 匹配到"Hello"
print(re.search(pattern, "She say Hello!")) # 无法匹配到
```
数据验证：
```python
import re

# 验证一个字符串是否是完全由数字组成的5位邮政编码
pattern = r"^\d{5}$"  # 意思是：从开头到结尾必须是恰好5位数字

print(re.search(pattern, "12345"))    # 匹配到
print(re.search(pattern, "1234"))     # 匹配不到（只有4位）
print(re.search(pattern, "123456"))   # 匹配不到（有6位）
print(re.search(pattern, "ABC12345")) # 匹配不到（开头有字母）
```

# Python字符串操作
## 字符串连接
```python
str1 = "hello"
str2 = "world"
str3 = str1 + str2
print(str3)
# 输出结果： helloworld

str4 = str1 + " " + str2
print(str4)
# 输出结果 hello world
```
## 索引与切片
**索引：**
```python
text = "Hello World"
# 正向索引
first_char = text[0]
print(first_char)
# 输出结果：H

# 负向索引
last_char = text[-1]
print(last_char)
# 输出结果：d
```
**切片：**
```python
# 切片格式[start:end:step] start是闭区间 end是开区间
text = "Hello World"
substring = text[0:4:1]
print(substring)
# 输出结果：Hell
every_other = text[::2]
print(every_other)
# 输出结果：HloWrd
reverse = text[::-1]
print(reverse)
# 输出结果：dlroW olleH
```
**长度计算**
```python
text = "Hello World"
str_len = len(text)
print(str_len)
# 输出结果：11
```
**大小写转换**
```python
text = "Pixiv Illustration"
# 全部转大写
text.upper()      # "PIXIV ILLUSTRATION"
# 全部转小写
text.lower()      # "pixiv illustration"
# 首字母大写
text.capitalize() # "Pixiv illustration"
# 每个单词首字母大写
text.title()      # "Pixiv Illustration"
# 大小写互换
text.swapcase()   # "pIXIV iLLUSTRATION"
```
## 搜索与替换
**查找子串**
```python
text = "Hi hello world, a beautiful day!"
# 查找子串首次出现位置find()
print(text.find("hel"))
# 输出结果：3

# 查找子串最后一次出现位置rfind()
print(text.rfind("a"))
# 输出结果：29

# 以特定字符串开头startswith()
print(text.startswith("Hi"))
# 输出结果True

# 以特点字符串结束endswitch()
print(text.endswith("day!"))
# 输出结果True
```
**子串计数**
```python
text = "Hi hello world, a beautiful day!"
print(text.count("y"))
# 输出结果：1
```
**替换内容**
```python
text = "Hello world!"
new_text = text.replace("Hello", "Hi") #注意，使用replace()后，原本的字符串内容不变，Python字符串具有不可变性
print(new_text)
# 输出结果：Hi world
print(text)
# 输出结果：Hello world

text = text.replace("Hello", "Hi") # 重新赋值了text，原本text的地址指向了text.replace("Hello", "Hi")
print(text)
# 输出结果：Hi world
```


## join函数详解
```join()```是Python字符串（str）类的一个方法，核心功能是将可迭代对象中的元素连接成字符串，使用该调用方法的字符串作为中间元素的分割符。
**参数要求：必须包含字符串元素的列表，元组，集合等**
```python
# 正确示例
tags = ["pixiv", "artwork"]
search_tag = " ".join(tags)
print(search_tag)
# 输出结果：pixiv artwork

# 错误示例
tags = [1, 2, 3]
search_tag = " ".join(tags)
print(search_tag)
# 输出结果：ypeError: sequence item 0: expected str instance, int found
```


## Python的路径导入方式
当写下import pixiv_api时，Python就如同快递员，它手里有一张地图列表（术语：sys.path），会按照顺序去这几个地方找名叫pixiv_api.py的文件。
寻址顺序：
1. 当前目录（Current Directory）: 也就是运行python xxx.py命令时所在的那个文件夹。
2. 标准库（Standard Library）: python自带的工具箱（如os, time, json）。如同“快递员的随身背包”
3. 第三方库（Site-packages）: 使用pip install 下载的库（如nonebot, aiohttp）
**常见的坑：**如果把自己的文件命名为random.py或者time.py，Python会先在当前目录找到文件，而不是去标准库找真正的random和time库，导致报错！一定不要使用标准库的名字去命名文件！

### 模块（Module） VS 包（Package）
**模块（Module）：**任何一个以.py结尾的文件就是一个模块
比如：一个具体的工具，就像“螺丝刀”

**包（Package）:**一个任何包含__init__.py文件的文件夹
比如：一个工具箱

### 两种核心导入方式（绝对 VS 相对）
```python
# 一个常见的nonebot的插件目录结构
my_project/             <-- 项目根目录
│
├── main.py             <-- 启动入口
└── plugins/            <-- 插件包
    ├── __init__.py
    ├── api/            <-- api 子包
    │   ├── __init__.py
    │   └── pixiv_api.py
    └── config/         <-- config 子包
        ├── __init__.py
        └── config.py
```
**1. 绝对导入（Absolute Import）-- “发全地址”**
不管在哪里，都从项目跟目录（sys.path的起点）开始写路径。
写法：```from plugins.api import pixiv_api```
优点：清晰，不容易出错。只要根目录不变，代码在哪里都能运行。

**2. 相对导入（Relative Impoprt）-- “给我旁边的人”**
这就是代码中点```.```的含义，它是基于当前文件所在位置来找文件的。
```.```一个点：代表当前文件夹
```..```两个点：代表上一级文件夹
例如```plugin/api/pixiv_api.py```中像导入```plugins/config/config.py```
```python
# 返回上一级（plugins）,再进入config文件夹，找config模块
from ..config import config
```
在```plugins/__init__.py```中导入```plugins/api/pixiv_api.py```中的```search_pixiv_by_tag```函数
```python
# 意思是：在当前文件夹（plugins）下，找api文件夹里的pixiv_api
from .api.pixiv_api import search_pixiv_by_tag
```
**模块导入的一个“天坑”**：相对导入（带点的）不能作为“主程序”（直接运行的脚本）中运行。如果直接运行```python plugins/api/pixiv_api.py```，会出现报错```ImportError: attempted relative import with no known parent package```原因：只有当这个文件呗别的程序导入时，它才知道它的“上一级”是谁。直接运行时，它自己就是老大，没有上一级。

### __init__.py的作用
1. 标记：它告诉Python，这个文件夹是一个包，不是普通的文件夹。
2. 暴露接口：
假设```pixiv_api.py```里面有一个函数名```download_image```
正常导入：```from plugins.api.pixiv_api import download_image```
如果在 ```api/__init__.py``` 里写：```from .pixiv_api import download_image```
外部就可以简写为：```from plugins.api import download_image``` (省掉了一层文件名)。
3. 初始化：到导入这个包时，```__init__.py```里的代码就会自动执行一次。例如可以在此处配置“用户白名单”，这意味着只要插件一加载，配置就生效了。

## 更高级的“寻址”技巧
代码示例：
```python
Path(__file__).parent.parent.parent.absolute()
DATA_DIR = BASE_DIR / "data"
TEMP_DIR = DATA_DIR / "pixiv_temp"
```
1. 核心锚点：```__file__```
第一步都是这个变量。```__file__```是Python的内置变量，代表当前这个代码文件自己的文件名（有时包含路径）。
比喻：就像在商场里看地图，地图上的红点代表“您在此处”
2. pathlib: 智能导航
（1）```Path(__file__)```
动作：把文件路径变成一个“智能对象”，不再是冰冷的字符串，现在拥有了“感知”周围环境的能力。
（2）```.parent```
动作：往上走一层文件夹
连用三次```.parent.parent.parent```：往上跳三级。这一行代码的意思是：“不管我在哪，请往上退三层，回到项目的根目录”。这样你就拿到了项目的总大门钥匙。
3. ```.absolute()```
动作：确保拿到的是全路径（从盘符开始），防止出bug。
4. ```BASE_DIR / "data"```
动作：路径拼接
解释：在```pathlib```里，除号```/```不再是除法，而是拼接符。
优点：写起来非常直观，就像写在文件路径的斜杠一样。

## Python的文件读取操作
找到了文件之后，下一步就是“打开并进行读取”
示例代码：
```python
if os.path.exists(character_file):
    try:
        with open(character_file, 'r', encoding='utf-8') as f:
            character_data = json.load(f)
    except Exception as e:
        logger.info(f"加载角色数据失败：{str(e)}")
```
示例代码包含了python的三个极其重要的技术点：
（1）上下文管理器（```with```语句） -- 资源的自动管家
（2）序列化（```json```模块） -- 数据的通用翻译官
（3）异常处理（```try...except```） -- 程序的防弹衣

第一部分：上下文管理器（```with```） -- 自动关门的强迫症管家
```with open(character_file, 'r', 'encodeing='utf-8') as f: ```
这段代码保证了：哪怕是读取json出错了，或者读完了，```f```文件句柄都会被自动关闭，释放系统资源。
（同理的，如代码```async with aiohttp.ClientSession() as session```它是帮助自动关闭网络连接）

第二部分：序列化```json``` -- 也就是“翻译”
读取的文件```character.json```本质上是一串字符串（文本）。Python看不懂字符串里的```{"key" : "value"}```代表字典。
此时需要一个翻译官。
**JSON(JavaScript Object Notation)**:互联网上最通用的数据交换格式。
```json.load(f)```：把文件里的文本，翻译成python的字典（dict）或者列表（list）。
比喻：把写在纸上的菜谱（文本），变成桌子上实实在在的菜（对象）
**配套的指令：**
```python
json.load(f) # 从文件读，变Python对象
json.dump(obj, f) # 把python对象，写进文件里
json.loads(s) # 从字符串读
json.dumps(obj) # 变字符串
```
第三部分：异常处理（try...except）  程序的防弹衣
在```__init__.py```中，用```try```包裹了读取文件的代码

```python
try:
    with open(...) as f:
        ...
    except Exception as e:
        logger.info(f"加载角色数据失败：{str(e)}")
```
如果不写```try...except```，一旦```character.json```格式出错，或者文件损坏，整个程序会直接crash，停止运行。

## Python网络编程核心
### 客户端（Client）与 服务端（Server）
互联网的一切交互，本质都是这两个角色的对话。
服务端（Server）:就像一家“24小时营业的超大仓库”。它存着无数的数据，它有一个固定的地址（IP/域名），时刻等着别人来取数据。
客户端（Client）:就像一个“快递小哥”。客户端的python代码就在控制该小哥，他的任务就是跑去仓库，说“我要这张图”，然后把图拿回来。
代码映射：```aiohttp.ClientSession()```这个名字里的```Client```就是指的客户端。

### IP地址与端口（PORT） -- 找门牌
形象理解：快递跑腿小哥（客户端）要出门，得知道往哪里走
1. IP地址（IP Address）:就是互联网上的“街道门牌号”
* pixiv的服务器有一个公网IP（比如```210.140.92.x```）
* 自己电脑也有一个IP
* 特殊IP：```127.0.0.1```，本地回环地址，代表着“我家”（localhost）
2. 端口（Port）:找到了大楼（IP），还需要知道去哪个窗口办事
* 网页服务通常在```80```或者```443```端口
* 端口可以自己定义
代码映射：```PROXY = http://127.0.0.1:7890```
翻译： 你的机器人不直接出国，而是把请求发给“我家地址 (127.0.0.1)”的“7890号窗口”。那里坐着你的代理软件（Clash/v2ray），它会帮你转发请求。

### HTTP协议（超文本传输协议） -- 填快递单的规矩
跑腿小哥到了仓库窗口，不能乱喊。他必须按照一套标准格式说话，这套格式就是HTTP协议。
一次完整的交互分为两步：**请求（Request）**和**响应（Response）**
1. 请求（Requests） -- 你发给服务器的单子。
一张标准的HTTP请求单包含以下部分：
URL（地址）：```https://......```
Method（动作）：你想干什么？
GET：“给我看看”（最常用，搜图，下图片）
POST：“给你这个”（登录时提交账号密码）
Headers(请求头\备注)：
```User-Agent```：告诉服务器“我是谁”。如果不写，默认是“Python-aiohttp”，服务器一看就知道是机器人，直接就踢出去。
```Referer```：告诉服务器“我是从哪里来的”。服务器会检查该项，防止盗取链接。
```Cookie```：“身份证明”。
