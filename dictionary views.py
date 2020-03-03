s1 = {1,2,3}
s2 = {2,3,4}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s2 -s1)

d1 = dict(zip('abc',[1,2,3]))
d2 = dict(zip('cde',[30,4,5]))
print(d1)
print(d2)

for key in d1:
    print(key)


for value in d1.values():
    print(value)

print(list(d1.values()))
print(list(d2.values()))


print(d1.items() | d2.items())
print(d1.items() - d2.items())

print(d1)
print(d2)
new_dict = {}
for key in d1.keys() & d2.keys():
    new_dict[key] = d2[key]
print(new_dict)
print(d1.keys() ^ d2.keys())


d1 = {'a':1,'b':2,'c':3,'d':4}
d2 = {'a':10,'b':20,'c':30,'d':40}

union = d1.keys() | d2.keys()
intersection = d1.keys() & d2.keys()
keys = union - intersection
results = {}
for key in keys:
    results[keys] = d1.get(key) or d2.get(key)
print(results)
