# from ipython_genutils.py3compat import xrange


def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        b = a + b
        yield b
        a = a + b

fs=fib_gen()
print(next(fs))
print(next(fs))
print(next(fs))


def factorial_gen():
    a=1
    b=1
    yield a
    while True:
        a= a * b
        b +=1
        yield a



#print("factorial ")
fs=factorial_gen()
print(next(fs))
print(next(fs))
print(next(fs))

print(next(fs))
print(next(fs))


print([ chr(i) for i in [65, 66, 67] ])