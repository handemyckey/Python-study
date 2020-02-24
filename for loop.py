# for  loop range

for i in range(5):
    print(i)

#for loop using list
for i in [7,8,9,6,4]:
    print(i)


# for loop for string
for c in 'Hello':
    print(c)


for x in ('a','b','c',4):
    print(x)

# for loop for tuples
for v,j in [(1,2),(3,4),(5,6),(7,8)]:
    print(v,j)

for i in range(5):
    if i ==3:
        break
    print(i)


# for in range with if else
for i in range (1,8):
    print(i)
    if i % 7 == 0:
        print('Multiple of 7 found')
        break
    else:
        print('NO multiple of 7 found in range')
