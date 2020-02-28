l = [1, 2, 3]
t = (1, 2, 3)
s = 'python'
print(l[0])

print(t[1])

print(s[2])

for c in s:
    print(c)

s = {10, 20, 30, 40, 50}
for e in s:
    print(e)

s = {'x','m',10,'v','d'}
for e in s:
    print(e)


l = [1,2,3]
t = (1,2,3)
print(l[0])
print(t[0])

l[0] = 100
print(l)
# t[0] = 200---- Tuple does not support item assignment
print(t)


s = "lucifer is a daemon"
print(list(enumerate(s)))
print(s.index('e'))


s = 'python'
l = [1,2,3,4,5,6,7,8,9,10]
print(s[1:4])
print(list(enumerate(s)))
print(l[0:5])
print(s[4:1000])

