def log(func):
    def inner(args):
        x=print("Accessed the function -'greet' with arguments ('{}',)".format( args)," {}")
        print(x)
        return func(args)
    return inner

@log
def greet(msg):
    print("stupid  ",msg)
    return msg

res_lst = list()
res_lst.append(greet(str(input())))
print("{}".format(*res_lst))