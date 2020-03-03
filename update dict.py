d = {'a':1,'b':2,'c':3}
d['b'] = 200

print(d)
d1 = {'a':1,'b':2}
d2 = {'c':3,'d':4}
d1.update(d2)
print(d1)
d1.update(b=20,x=40,c=30)
print(d1)


d1 = {'a':1,'b':2}
d1.update((k, ord(k)) for k in 'python')
print(d1)


l1 = [1,2,3]
l2 = 'abc'
l = (*l1,*l2)
print(l)


d1 = {'a':1,'b':2}
d2 = {'b':20,'d':4}
d3 = {'b':200,'d':40,'e':5}
d = {**d1, **d2, **d3}
print(d)
conf_defaults = dict.fromkeys(('host','port','user','pwd','database'),None)
print(conf_defaults)

conf_global = {'port':5432,'database':'Deepdive'}

conf_dev= {
    'host':'localhost',
     'user' : 'test',
    'pwd' : 'test'
}

conf_prod = {
    'host' : 'prodg.deepdive.com',
    'user' : '$prod_user',
    'pwd' : '$prod_pwd',
    'database' : 'deepdive_prod'
}

    #conf_defaults-->global-->dev / prod

conf = {**conf_defaults, **conf_global, **conf_dev}
print(conf)
conf = {**conf_defaults, **conf_global, **conf_prod}
print(conf)


def my_func(*,kw1,kw2,kw3):
    print(kw1,kw2,kw3)
d = {'kw2':20,'kw1':10,'kw3':10}
my_func(**d  )
