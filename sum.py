L = range(1,101)
n=0
while n<100:
    L[n]=L[n]*L[n]
    n=n+1
print sum(L)