def coroutine_decorator(func):
    def wrapper(*args, **kwdargs):
        c = func(*args, **kwdargs)
        next(c)
        return c
    return wrapper


@coroutine_decorator
def linear_equation(a,b):
    x=0

    while True:
        try:
            x=yield
            z= a*x**2 +b
            print("Expression, {}*x^2 + {}, with x being {} equals {}".format(a, b, x, z))
        except StopIteration as e :
            print(e)
            break


@coroutine_decorator
# @coroutine_decoratorforNumber
def numberParser():
    try :
        x=yield
        eq1=linear_equation(3,4)
        eq1.send(x)
        eq2=linear_equation(2,-1)
        eq2.send(x)
    except StopIteration:
        pass

def main(x):
    n=numberParser()
    try:
        n.send(x)
    except StopIteration as e:
        pass

main(6)

