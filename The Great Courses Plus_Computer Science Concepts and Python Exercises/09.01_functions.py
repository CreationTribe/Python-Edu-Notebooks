def warn():
    print("Warning! Use at your own risk.")
    ans = input("Do you want to continue? (Y/N): ")
    if ans == 'n' or ans == 'N':
        quit()


def get_sum(x):
    sum = 0
    for i in range(x+1):
        sum += i
    return sum


def factorial(n):
    product = 1
    for i in range(1, n+1):
        product = product*i
    return product


print(factorial(20))


def sum_list(mylist):
    """Sums and alters list accordingly"""
    for i in range(1, len(mylist)):
        mylist[i] += mylist[i-1]
    return mylist[len(mylist)-1]


minmaxlist = [1, 2, 3, 4, 66, 55, 33, 22, 234, 98, 457, 4, 98, 46, 546, 2346, 6, 3]
print(min(minmaxlist))
print(max(minmaxlist))