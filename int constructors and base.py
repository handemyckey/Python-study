import fractions

a = fractions.Fraction(22, 7)
print(a)


def from_base10(n,b):
    if b < 2:
        raise ValueError('Base B must be >= 2')
    if n < 0:
        raise ValueError('Number n mujst be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        n , m= divmod(n,b)
        digits.insert(0,m)
    print(digits)

from_base10(10,2)
from_base10(255, 16)
from_base10(64,8)


def encode(digits,digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode the digits")
    encoding=''
    for d in digits:
        encoding += digit_map[d]
    print(encoding)

encode([15,15],'0123456789ABCDEF')