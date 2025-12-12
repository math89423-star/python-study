text = "Hello world!"
new_text = text.replace("Hello", "Hi") #注意，使用replace()后，原本的字符串内容不变，Python字符串具有不可变性
print(new_text)
# 输出结果：Hi world
print(text)
# 输出结果：Hello world

text = text.replace("Hello", "Hi") # 重新赋值了text，原本text的地址指向了text.replace("Hello", "Hi")
print(text)
# 输出结果：Hi world