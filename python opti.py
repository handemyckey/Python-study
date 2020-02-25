a = 5130
b = 5130
print(id(a))
print(id(b))


print(a is b)


c = 'Hello_world'
d = 'Hello_world'
print(id(a),id(b))
print(a is b)


# String intern
import sys
a = sys.intern('Hello world')
b = sys.intern('Hello world')
c = 'Hello world'
print(id(a),id(b),id(c))
print(a == b)
print(a is b)




def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
            if a == b:
                pass


def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
            if a is b:
                pass


import time
start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print('Equality:-',end-start)


