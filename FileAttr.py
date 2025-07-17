import ctypes as c
from os import _exit as exit
def SetFileAttribute(name, attributes : int):
    try:
        kernel32 = c.CDLL("Kernel32.dll")
        return kernel32.SetFileAttributesA(name, attributes)
    except(PermissionError, Exception):
        print("File is Used by Any Program or It is Read-Only File!!! Pls Close All Unused Program or Used Program what opened engine_config.txt!!!")
        exit(3221)
