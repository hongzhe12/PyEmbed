import subprocess

# 设置 Python 解释器路径和脚本路径
python_exe = ".\\python-embed\\pythonw.exe"
script_path = ".\\src\\main.py"

# 使用 subprocess 非阻塞执行，隐藏 DOS 窗口
process = subprocess.Popen([python_exe, script_path], creationflags=subprocess.CREATE_NO_WINDOW)

# 不等待进程结束，直接继续执行后续代码
print("Python script is running in the background...")
