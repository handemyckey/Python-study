#3 You have multiple servers analyze data and dictionary that contains words and frequency
d1 = {'python':10,'java':3,'c#':8,'javascript':15}
d2 = {'java':10,'c++':10,'c#':4,'go':15,'python':6}
d3 = {'erlang':5,'haskell':2,'python':1,'pascal':1}

def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k,v in d.items():
            unsorted[k] = unsorted.get(k,0) + v
    print(unsorted)

merge(d1,d2,d3)


def merge1(*dicts):
    sorted1 = {}
    for d in dicts:
        for k,v in d.items():
            sorted1[k] = sorted1.get(k,0) + v
    print(dict(sorted(sorted1.items(), key=lambda el:el[1])))

merge1(d1,d2,d3)


