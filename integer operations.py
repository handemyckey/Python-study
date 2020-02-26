import math

print(math.floor(-3.9999))  # floor of negative number will not be ame as of positive number
print(math.floor(3.9999)) # floor value of positive number will always be <= number


a = 33
b = 16
print("\n\n",a/b)
print(a//b)
print(math.floor(a/b))


a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
# Output
# -2.0625
# -3
# -3

a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
print(math.trunc(a/b))
# Output
# 2.0625
# -3
# -3
# -2

#a = b * (a//b) + (a%b)
a= 13
b = 4
print('{0}/{1} = {2}'.format(a,b,a/b))
print('{0}//{1} = {2}'.format(a,b,a//b))
print('{0}%{1} = {2}'.format(a,b,a%b))
print(a == b * (a//b) + (a%b))
# Output
# 13/4 = 3.25
# 13//4 = 3
# 13%4 = 1
# True

a = int(10.9) # It gets truncated
print(a)

b = int("10")
print(b)




