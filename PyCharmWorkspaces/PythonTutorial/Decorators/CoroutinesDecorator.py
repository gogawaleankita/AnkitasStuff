def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper




@coroutine_decorator
def TokenIssuer(tokenId=0):
    try:
        while True:
            name = yield
            tokenId += 1
            print('Token number of', name, ':', tokenId)
    except GeneratorExit:
        print('Last issued Token is :', tokenId)
t = TokenIssuer(100)
t.send('George')
t.send('Rosy')
t.send('Smith')
t.close()