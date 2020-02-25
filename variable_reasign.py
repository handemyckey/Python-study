# If you store same value in 2 variable it will point to same location
# If we change the variable value aor reassign the value it will refere to new value old value will remain as it is in location
a = 10
b = 10
c = 10
print("memory address:- ",hex(id(a)))
print(type(a))
print("memory address:- ", hex(id(b)))
print(type(b))
print("memory address:- ", hex(id(c)))
print(type(c))


