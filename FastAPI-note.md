# FastAPI学习
## 安装FastAPI
```pip install fastapi```
## FastAPI使用步骤
示例代码：
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root() -> dict:
    return {"message": "Hello World"}
```

1. 导入```FastAPI```: 
```from fastapi import FastAPI```

```FastAPI```是一个为你的API提供了所有功能的Python类。

2. 创建一个```FastAPI```实例:
```app = FastAPI()```
这里的变量```app```会是```FastAPI```类的一个实例，这个实例将是创建所有API的主要交互对象。

3. 创建一个路径操作：
**路径**
这里的路径指的是URL中从第一个```/```起的后半部分。所以再一个这样的URL中：
```https://example.com/items/foo```
路径会是：```/items/foo```
路径也称为端点或**路由**，开发API时，路由是用来分离关注点和资源的主要手段。
**操作**
这里的操作指的是一种HTTP方法。下列之一：
```python
· POST
· GET
· PUT
· DELETE
# 较为少见的
· OPTIONS
· HEAD
· PATCH
· TRACE
```
在http协议中，可以使用以上一种或多种方法与每个路径进行通信。
比较常用的：
```python
POST: 创建数据
GET: 读取数据
PUT：更新数据
DELETE： 删除数据
```
**定义一个路径操作器**
```@app.get("/")```告诉FastAPI在它下方的函数负责处理如下访问请求：
· 请求路径为```/```
· 使用```get```操作
```python
# info : 
@something 语法在Python中被称为装饰器
如同一顶装饰帽，将它放在函数的上方，装饰器接收位于其下方的函数并且用它完成一些工作。
在例子中，装饰器告诉FastAPI位于其下方的函数对应着路径/加上get操作
它是一个**路径操作装饰器**
```

4. 定义路径操作函数
路径：```/```
操作：```get```
函数：是位于装饰器下方的函数
```async def root() -> dict:```
每当FastAPI接收一个使用GET方法访问URL```/```的请求时这个函数会被调用。
这个例子中，路径操作函数是async函数，常规函数也可以。

5. 返回内容
``` return {"message": "hello world"}```

## 路由
在 FastAPI 中，/items/{item_id} 和 /items/{item_id}/ 这两个路由的主要区别在于URL末尾的斜杠（/）。这不仅仅是一个书写习惯的差异，它直接影响着路由的匹配规则和客户端的行为。
| 特性 | "/items/{item_id}"(无末尾斜杠) | "/items/{item_id}/"(末尾有斜杠) |
| :---- | :--------------------------- | :----------------------------- |
| 路由匹配 | 精确匹配，仅匹配.../items/123 | 目录匹配，匹配.../items/123/ 及其所有子路径，如.../items/123/details
| 重定向行为 | 访问.../items/123/ 会返回404 Not Found | 访问.../items/123, FastAPI默认自动重定向307到带斜杠版本 |
| 设计语义 | 通常指向一个具体的资源对象，如一件商品 | 通常被视为一个资源目录或集合入口 | 



## 路径参数
FastAPI支持使用Python字符串格式化语法声明路径参数（变量）
```python
@app.get("/items/{item_id}")
async def read_item(item_id: str) -> dict:
    return {"item_id": item_id}
```
这段代码把路径参数item_id的值传递给路径函数的参数item_id.
运行示例并访问：```http://127.0.0.1:8000/items/foo```可以得到如下回应：
```{"item_id": "foo"}```
若定义的item_id为int，输入字符串则会报错：
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int) -> dict:
    return {"item_id": item_id}

# 访问http://127.0.0.1:8000/items/foo，会出现报错：
# {"detail":[{"type":"int_parsing","loc":["path","item_id"],"msg":"Input should be a valid integer, unable to parse string as an integer","input":"foo"}]}
```
要注意顺序
比如要使用```/users/me```获取当前用户的数据，然后用```/users/{user_id}```，通过用户ID获取指定用户的数据。由于路径操作是按顺序的，因此，一定要在```/users/{user_id}```之前申明```/user/me```:
```python

from fastapi import FastAPI

app = FastAPI()

@app.get("/user/me")
async def read_user_me() -> dict:
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
```

使用python的枚举类型
举例：
```python
from enum import Enum
from fastapi import FastAPI

class ModeName(str, Enum):
    MODE_A = "mode_a"
    MODE_B = "mode_b"
    MODE_C = "mode_c"


app = FastAPI()

@app.get("/mode/{mode_name}")
async def get_mode(mode_name: ModeName) -> dict:
    return {"selected_mode": mode_name}

# 只能访问http://127.0.0.1/8000/mode/mode_a | http://127.0.0.1/8000/mode/mode_b | http://127.0.0.1/8000/mode/mode_c
# 访问其他会报错
```
**比较枚举元素**，枚举类```ModeName```中的枚举元素支持比较操作：
```python
from enum import Enum

from fastapi import FastAPI


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}
```
路径转换器
直接使用 Starlette 的选项声明包含路径的路径参数：
```/file/{file_path:path}```
本例中，参数名为 file_path，结尾部分的 :path 说明该参数应匹配路径。
```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}

# 如文件地址：C:\Users\Administrator\Desktop\python学习\python-comfyui\default.conf
# 访问url：http://127.0.0.1:8000/files//C:/Users/Administrator/Desktop/python%E5%AD%A6%E4%B9%A0/python-comfyui/default.conf 
# 注意//部分
```

## 查询参数
当声明的参数不是路径参数时，路径操作函数会把该参数自动解释为查询参数
```python
from fastapi import FastAPI

app = FastAPI()

fake_items = [{"item_name":"Foo"}, {"item_name":"Bar"}, {"item_name":"Baz"}]

@app.get("/items")
async def read_item(skip: int = 1, limit: int = 2) -> list:
    return fake_items[skip : skip + limit]

# 访问URL：http://127.0.0.1:8000/items?skip=1&limit=2
```

## 请求体
FastAPI使用请求体从客户端（例如浏览器）向API发送数据
请求体是客户端发送给API的数据。响应体是API发送给客户端的数据。
API 基本上肯定要发送响应体，但是客户端不一定发送请求体。
使用 Pydantic 模型声明请求体，能充分利用它的功能和优点。
```info : 发送数据使用 POST（最常用）、PUT、DELETE、PATCH 等操作。```

```python
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None  # 不能使用 str or None = None
    price: float
    tax: float | None = None

app = FastAPI()

@app.post("/items")
async def create_item(item: Item) -> dict:
    item_dict = item.model_dump()
    if item.tax != None:
        total_price = item.price + item.tax
        item_dict.update({"total_price": total_price})
    return item_dict
```

**解包操作符**（**）
单个星号 * 用于解包列表或元组，而双星号 ** 用于解包字典。
它的作用是将一个字典的“键-值”对展开，就好像是直接作为关键字参数（key=value）写在那里一样：
```python
# 假设有字典
item_dict = {'name': 'Widget', 'price': 9.99}

# 这行代码...
new_dict = {"item_id": 123, **item_dict}

# ...等价于直接写：
new_dict = {"item_id": 123, 'name': 'Widget', 'price': 9.99}
```

## 查询参数和字符串校验
FastAPI允许为参数声明额外的信息和校验，如添加约束条件：即使 q 是可选的，但只要提供了该参数，则该参数值不能超过50个字符的长度。
```python
from fastapi import FastAPI, Query
from typing import Union

app = FastAPI()

@app.get("/items/")
async def read_items(q: Union[str, None] = Query(default=None, min_length=3, max_length=50, regex="^fixedprefix_")):
    results: dict = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
# 将 Query 用作查询参数的默认值，并将它的 max_length 参数设置为 50
# 用 Query(default=None) 替换默认值 None，Query 的第一个参数同样也是用于定义默认值
# q: Union[str, None] = Query(default=None) 等同于 q: str = None
```
**数据校验：大于和小于等于**
```python
# gt: 大于（greater than）
# ge: 大于等于（greater than or equal）
# lt: 小于（less than）
# le: 小于等于（less than or equal）


from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_items(
    *,
    item_id: int = Path(title = "The ID of the item get", gt = 0, le = 10000),
    q: str
) -> dict:
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
```

## 多个请求体参数
可以添加多个请求体参数到路径操作函数中，即使一个请求只能有一个请求体。
但是 FastAPI 会处理它，在函数中为你提供正确的数据，并在路径操作中校验并记录正确的模式。
还可以声明将作为请求体的一部分所接收的单一值。
还可以指示 FastAPI 在仅声明了一个请求体参数的情况下，将原本的请求体嵌入到一个键中。

路径操作中可以声明多个请求体参数，例如```item```和```user```：
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User) -> dict:
    results = {"item_id": item_id, "item": item, "user": user}
    return results
```

## HTTP Headers
HTTP头部是客户端和服务器在HTTP请求和响应中传递的元数据，用于传递附加信息。它们由键值对祖成，例如：```Content-Type: application/json```
常见的HTTP头部字段：
```Content-Type```：指定请求或响应体的媒体类型，如```application/json```、```text/html```
```User-Agent```：标识客户端软件（如浏览器类型和版本）
```Cookie```：  客户端发送的存储数据，用于会话管理
```Set-Cookie```：服务器指令，用于在客户端设置Cookie
```Authorization```：包含认证凭证，如Bearer令牌

**获取Header:**
FastAPI的request对象包含了HTTP请求的所有信息，可以在路由函数中注入Request对象，通过request.headers属性访问请求头。
```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/headers")
async def read_headers(request: Request) -> dict:
    headers = request.headers
    return dict(headers)
```

## Cookie
由于HTTP协议本身是无状态的，服务器默认无法区分连续的请求是否来自同一客户端。Cookie的出现正是为了解决HTTP无状态的问题，它允许服务器给客户端下发一个小的文本片段（Cookie），客户端会在后续的请求中自动携带这个片段，从而让服务器能够“记住”客户端的某些信息。

**Cookie的工作原理​：**
​1. 首次请求​：客户端（如浏览器）访问服务器。
​2. 服务器设置Cookie​：服务器通过响应头中的Set-Cookie字段，要求客户端存储特定信息。
​3. 客户端存储​：客户端将Cookie保存起来。
​4. 后续请求​：客户端向同一服务器发起的每一次请求，都会自动通过Cookie请求头将这些信息带回给服务器。

**Cookie的关键属性**
1. 名称(Name)和值(Value)​​：存储的实际数据。
2. 域(Domain)和路径(Path)​​：定义了Cookie可被哪些URL访问。
3. ​过期时间(Expires/Max-Age)​​：控制Cookie的有效期。不设置则通常为会话Cookie（浏览器关闭即失效）。
4. ​安全标志(Secure & HttpOnly)​​：Secure要求仅通过HTTPS传输；HttpOnly可阻止JavaScript访问，增强安全性。

**Cookie操作**
```python
from fastapi import FastAPI, Response, Cookie
from typing import Optional

app = FastAPI()

@app.get("/login")
def login(response: Response):
    # 服务器设置Cookie
    response.set_cookie(key="username", value="user123", max_age=3600, httponly=True)
    return {"message": "Login successful, cookie set"}

@app.get("/profile")
def get_profile(username: Optional[str] = Cookie(None)): # 从请求中提取Cookie
    if not username:
        return {"error": "Not logged in"}
    return {"message": f"Welcome back, {username}"}
```

## 导入Cookie
定义 Cookie 参数与定义 Query 和 Path 参数一样。
```python
from typing import Annotated

from fastapi import Cookie, FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    return {"ads_id": ads_id}
```

## User-Agent：客户端的"身份证"
User-Agent是HTTP请求头中的一个特殊字段，它包含了描述客户端软件（如浏览器、应用程序、爬虫脚本）的字符串。这个字符串通常包括操作系统、浏览器类型和版本、渲染引擎等信息。

**User-Agent的主要作用​：**
1. 内容协商​：服务器根据User-Agent返回最适合该客户端的内容，例如，为移动端返回移动版页面，为桌面端返回PC版页面。
2. 统计与分析​：网站通过分析User-Agent来了解用户的设备分布和浏览器使用情况。
3. 爬虫识别与反爬​：网站管理员可通过User-Agent识别爬虫流量，并采取允许或限制措施；而爬虫程序则可通过设置常见的浏览器User-Agent来尝试“伪装”成普通浏览器。

**设置User-Agent**
当你使用requests库发送HTTP请求时，默认的User-Agent会标识自己为python-requests/x.x.x（其中x.x.x是版本号）。有些网站可能会拒绝此类非浏览器客户端的请求。这时，你可以通过自定义Header来模拟浏览器访问：
```python
import requests

url = 'https://httpbin.org/user-agent' # 一个用于测试的API

# 默认的User-Agent（通常会暴露是Python脚本）
response_default = requests.get(url)
print("Default User-Agent:", response_default.json()['user-agent'])

# 自定义User-Agent，模拟Chrome浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
response_custom = requests.get(url, headers=headers)
print("Custom User-Agent:", response_custom.json()['user-agent'])
```


## 响应码