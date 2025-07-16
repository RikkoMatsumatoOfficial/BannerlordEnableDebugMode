import ctypes as c

def SetFileAttribute(name, attributes : int):
    kernel32 = c.CDLL("Kernel32.dll")
    return kernel32.SetFileAttributesA(name, attributes)