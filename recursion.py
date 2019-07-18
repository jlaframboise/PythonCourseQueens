def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

def combo(n,r):
    return fact(n)//fact(n-r)*fact(r)

def perm(p,r):
    return fact(p)//fact(p-r)

# not very efficient
def rfib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    a,b = 0,1
    for x in range(n):
        b, a = a+b, b
    return b

for x in range(1000):
    print(fib(x))