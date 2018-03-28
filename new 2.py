def mout(x):
    if x==1:
        return 1
    if x!=1:
        return x*mout(x-1)

print mout(10)

