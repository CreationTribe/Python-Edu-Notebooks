# This is a terrible way to crunch fibonacci
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


def fibo(n):
    F = [0, 1]
    for i in range(2, n+2):
        F.append(F[-2] + F[-1])
    return F[n]


print(fibo(100))
