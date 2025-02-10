import ctypes

# 加载user32.dll库，该库包含了许多Windows用户界面相关的函数
user32 = ctypes.windll.user32

result = user32.MessageBoxW(None, "Hello, World!", "Message", 0)
