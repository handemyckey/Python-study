# Everything in python is object

a = 10
print(type(a))

b = int(10)
print(b)
print(type(b))


def square(a):
    return a ** 2



print(type(square))

f = square
print(id(square))

print(id(f))

print(f is square)
square(2)


def cube(a):
    return 2 ** 3



cube(3)


def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

f = select_function(1)
print(f is square)

f = select_function(2)
print(f is cube)


print("ANS :",select_function(1)(4))
