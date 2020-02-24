# add while loop

i = 5
while i <= 5:
        print(i)
        i += 1
        break


# while true with break
i = 5
while True:
    print(i)
    if i >= 5:
        break
        pint("Value of I is greater or equal to 5" )


# while loop with continue
a = 0
while a < 10:
    a += 1
    if a%2 == 0:
        continue
    print(a)


# break with append
l = [1,2,3,10]
val = 152
idx = 0
while idx < len(l):
    if l[idx] == val:
        break
    idx += 1
else:
    l.append(val)

print(l)
