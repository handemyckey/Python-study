a = 10
b = 10
print(id(a))
print(id(b))

print("a is b", a is b)
print("a == b", a == b)


a = 500
b = 500.00
print("a is b", a is b)


print(id(None))