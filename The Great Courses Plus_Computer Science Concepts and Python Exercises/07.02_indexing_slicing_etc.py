# https://www.geeksforgeeks.org/python-string-interpolation/
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/

list1 = [3.1, 1.2, 5.9]
list2 = [3.0, 2.5]

plus_list = list1 + list2

list1 += list2

list1.append(4.4)

print(*list1, sep='\n')

print(list1[-1])

tlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
tlist[0:0:] = [100, 200, 300, 400, 500, 600]

# copy a slice to a new variable
tclist = tlist[:]

# set the new list's slice to empty, and it will cut the middle out
tclist[5:10] = []

# [Start:Stop:Slice]
print(tclist)


# print(str(a)[1:-1])


# # AGE example
# ages = []
# age = int(input("enter an age or a group member. Enter -1 when done"))
#
# while age != -1:
#     ages.append(age)
#     age = int(input("Enter an age or a group member. Enter -1 when done"))
