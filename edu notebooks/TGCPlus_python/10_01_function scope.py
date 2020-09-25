def maxdemo(v1, v2):
    if v1 > v2:
        return v1
    else:
        return v2


a = 1
b = 2

print(maxdemo(a, b))

# global variables


def playingglobal():
    global monkey # allows you to declare a global
    monkey = 'ducks'


playingglobal()

print(monkey)

# no pass by reference in python
# list is mutable: can be changed inside a function
# int float string are all immutable:

list1 = [1, 2, 3, 4]
list2 = [55, 66, 77, 88]

list3 = list1 # copy by reference - it's pointing to the exact same list as list1
list3 += list2

print(list1)


def mutinglists(v1, v2):
    v1 += v2


mutinglists(list1, list2)

print(list1)


def calcmiles(gallons, mpg=2.5):
    return gallons * mpg


print(calcmiles(44))
print(calcmiles(44, 4))


def madlib(animal='dog', adj='green', city='denver', food='carrot'):
    return "A " + adj + ' ' + animal + " in " + city + " was eating a " + adj + ' ' + food


print(madlib())
print(madlib("monkey"))
print(madlib(adj="drunk"))
print(madlib("monkey", "ugly"))
print(madlib("monkey", "ugly", "SLC"))
print(madlib("monkey", "ugly", "SLC", "dick-juice"))


























