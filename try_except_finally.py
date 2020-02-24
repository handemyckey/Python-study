# try except and finally
a = 10
b = 0

try:
    a/b
except ZeroDivisionError:
    print('division by 0')
finally:
    print('This always works')

# ZeroDivisionError
a = 0
b  = 2

while a < 4:
    print('--------------------')
    a += 1
    b -= 1

    try:
        a/b
    except ZeroDivisionError:
        print("{0},{1} - division by 0" .format(a,b))
        continue
    finally:
        print("{0},{1} - Always Executes" .format(a,b))

    print("{0},{1} - main loop".format(a, b))
else:
    print("Code executes without a zero division error")