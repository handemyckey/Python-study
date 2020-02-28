#Fib(n) = Fib(n-1) + Fib(n-2)
#Fib(0) = 1
#Fib(1) = 1

def fib_recursive(n):
    if n <= 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

print([fib_recursive(i) for i in range(7)])


from timeit import timeit
print(timeit('fib_recursive(10)', globals = globals(), number=10))

print(timeit('fib_recursive(28)', globals=globals(), number=10))

print(timeit('fib_recursive(29 )', globals=globals(), number=10))


def Fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n-1):
        fib_0 , fib_1 = fib_1, fib_0 + fib_1
    print(fib_1)

print([Fib(i) for i  in range(7)])


#def fib(i):
   # pass

import math
class FibIterr:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        else:
            result = Fib(self.i)
            self.i += 1
            return result
fib_iter = FibIterr(7)



def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1

gen = fib(7)
for num in gen:
    print(num)

