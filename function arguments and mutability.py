def process(s):
    print("Initial memory Address s = {0}".format(id(s)))
    s = s + 'World'
    print("Final memory Address s = {0}".format(id(s)))
    print(s)

my_var = 'hello'
print('my_var  = {0}'.format(id(my_var)))

process(my_var)

print(id(my_var))

