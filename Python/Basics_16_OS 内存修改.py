import win32gui
import win32api
import win32process
import ctypes

# 定义一个全局变量，设置未系统最高权限
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

# 找窗体，获得句柄
win = win32gui.FindWindow("MainWindow", "植物大战僵尸中文版")

# 根据句柄找到进程号
hid, pid = win32process.GetWindowThreadProcessId(win)

# 以最高权限打开进程
p = win32api.OpenProcess(PROCESS_ALL_ACCESS, False, pid)

# 加载内核模块
md = ctypes.windll.LoadLibrary("C:/Windows/System32/kernel32.dll")

# 定义一个C语言的long类型
data = ctypes.c_long()

# 读取内存,int(p):p进程；211944712:内存地址；ctypes.byref(data):保存位置;4:四个字节；None:报错信息
md.ReadProcessMemory(int(p), 211944712, ctypes.byref(data), 4, None)

print(data)

# 修改内存
newData = ctypes.c_long(1000)
md.WriteProcessMemory(int(p), 211944712, ctypes.byref(newData), 4, None)
