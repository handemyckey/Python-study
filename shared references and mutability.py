a = [1,2,3,4]
b = a
c  = "hello world"
print("Address of a :",hex(id(a)))
print("Address of b :",hex(id(b)))
print("Address of c :",hex(id(c)))

b.append(100)
print(a)