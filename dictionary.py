a = {'k1': 100, 'k2':200}
print(type(a))
print(a)

print(hash((1,2,3)))

d = {(1,2,3): 'this is a tuple'}
print(d[1,2,3])

t1 = (1,2,3)
t2 = (1,2,3)
print(t1 == t2)
print(hash(t1) == hash(t2))
print(t1 is t2)
print(id(t1),"\n",id(t2))
print(d[t1])
print(d[t2])


d = dict(zip('abc',range(1,4)))
print("\n",d)
print(len(d))
print(d.get('a'))
result = d.get('python')
print(type(result))



text = 'lucifer Is a daemons name'
counts = dict()
for c in text:
    counts[c] = counts.get(c, 0)+1
print(counts)

data = 'kingslayer killled the mad king GOT'
count = dict()
for c in data:
    key = c.lower().strip()
    if key:
        count[key] = count.get(key, 0) + 1
print(count)



d = {'a':1,'b':2,'c':3,'z':0}
def insert_if_not_present(d,key,value):
    if key not in d:
        d[key] = value
        print(value)
    else:
        print(d[key])
insert_if_not_present(d,'z',100)



import string
print(string.ascii_lowercase)
print(string.ascii_uppercase)


categories = {}
for c in text:
    if c!= '':
        if c in string.ascii_lowercase:
            key = 'lower'
        elif c in string.ascii_uppercase:
            key = 'upper'
        else:
            key = 'other'
        categories.setdefault(key, set()).add(c)
        #if key not in categories:
        #categories[key] = set()
        #categories[key].add(c)
for cat in categories:
    print(f'{cat}:', ''.join(categories[cat]))



def cat_key(c):
    if c == '':
        print("None")
    elif c in string.ascii_lowercase:
        print("Lower")
    elif c in string.ascii_uppercase:
        print("Upper")
    else:
        print("Other")

categories = {}
for c in text:
    key = cat_key(c)
    if key:
        categories.setdefault(key,set()).add(c)

    for cat in categories:
        print(f'{cat}:',''.join(categories[cat]))