## Python头文件的相对导入与绝对导入
```from .base_python_function import *```
是相对导入，表示从当前包（同一包内的模块）导入。
只能在包上下文中使用（目录含有效包名且有 init.py），不能直接用 python base_python.py 作为脚本执行，否则会报错：```ValueError: attempted relative import with no known parent。```

```from base_python_function import *```
是绝对导入，Python 会在 sys.path（当前工作目录、PYTHONPATH、site-packages 等）中查找模块。
直接运行脚本（python base_python.py）时通常可用（前提是模块文件与脚本在同一目录，或该目录在 sys.path 中）。