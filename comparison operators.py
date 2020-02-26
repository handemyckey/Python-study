print(0.1 is (3+4j))

print(3 is 3)

print([1,2] is [1,2])

print('a' in 'This is a test')

print(3 in [1,2,3])

print(3 not in [1,2,3])

print('key1' in {'key1':1})

print(1 in {'key1':1})

from decimal import  Decimal
from fractions import Fraction

print(4 < Decimal('10.5'))

print(Fraction(2,3) < Decimal('0.5'))

print(4 == 4 + 0j)

print(True == Fraction(2,2))

print(True < Fraction(3,2))

print(1 < 2 < 3)

print(1 < 2 and 2 < 3)

print(3 < 2 < 1/0)

print(1 < 2 > -5 == Decimal('-5.0'))

import string
print('A' < 'a' < 'z' > 'Z' in string.ascii_letters)


