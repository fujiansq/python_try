def func1(arg1,arg2):
    if arg1 == 0:
        #print arg1,arg2
        pass
    arg3 = arg1 + arg2
    if arg3 > 1000:
        return arg3
    return func1(arg2,arg3)

result = func1(0,1)
print result