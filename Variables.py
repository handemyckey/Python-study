#Reference Count to a variable
import sys
a = [1,2,3,3,8,44,1]
print("Address: ",id(a))
print("Reference Count: ",sys.getrefcount(a))


import ctypes
def ref_count(address : int):
    return ctypes.c_long.from_address(address).value
print("\n\nAddress: ",id(a))
print("Ref Count:",ref_count(id(a)))
