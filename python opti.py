a = 5130
b = 5130
print(id(a))
print(id(b))

print(a is b)

c = 'Hello_world'
d = 'Hello_world'
print(id(a), id(b))
print(a is b)

# String intern
import sys

a = sys.intern('Hello world')
b = sys.intern('Hello world')
c = 'Hello world'
print(id(a), id(b), id(c))
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
print('Equality:-', end - start)


# peephole intern
# constant expressions
def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown box' * 5
    f = ['a', 'b'] * 3
    print("\n", a, "\n", b, "\n", c, "\n", d, "\n", e, "\n", f)


my_func()


def my_func(e):
    if e in [1, 2, 3]:
        pass
my_func(2)




import string
import time

string.ascii_letters
'abcdftjsjndkjsdbhikurgdjbzajfhkJDFHKDJIXBNSJGWjfhkafhjjhakfjyarAFHWIKDUHJFK'
char_list = list(string.ascii_letters)
print("\n\n",char_list,"\n\n")

char_tuple = tuple(string.ascii_letters)
print(char_tuple,"\n\n\n")

char_set = set(string.ascii_letters)
print(char_set,"\n\n\n")



def membership_test(n, container):
    for i in range(n):
        if 'x' in container:
            pass

#time required for execution of list
start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print("List:", end-start)

#time required for execution of tuple
start_1 = time.perf_counter()
membership_test(10000000, char_tuple)
end_1 = time.perf_counter()
print("tuple:", end_1-start_1)

#time required for execution of set
start_2 = time.perf_counter()
membership_test(10000000, char_set)
end_2 = time.perf_counter()
print("Set:", end_2-start_2)



