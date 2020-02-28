def my_func(a,b):
    c = a + b
    print(c)
x = 10
y = 6
my_func(4,6)


def check_sum(*args):
    *_, a,b = args
    add = a + b
    return add
print(check_sum(20,40,60,40))



# Positional & keyword arguments
def my_func(a,b,c):
    print("a = {0}, b = {1}, c = {2}".format(a,b,c))

my_func(5,6,7)
