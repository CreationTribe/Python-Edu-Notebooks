# Recursion
#   merge sort
def merge(xlist, listA, listB):
    i = 0
    j = 0
    k = 0

    while j < len(listA) or k < len(listB):
        if j < len(listA):
            if k < len(listB):
                # not at the end of listA or listB, so pull smaller value
                if listA[j] < listB[k]:
                    xlist[i] = listA[j]
                    j += 1
                else:
                    xlist[i] = listB[k]
                    k += 1
            else:
                # at the end of listB, so focus on listA
                xlist[i] = listA[j]
                j += 1
        else:
            # end of listA so focus on listB
            xlist[i] = listB[k]
            k += 1
        i += 1
    return


def merge_sort(xlist):
    xcount = len(xlist)

    if xcount <= 1:
        return
    sublist1 = xlist[:xcount//2]
    sublist2 = xlist[xcount//2:]
    merge_sort(sublist1)
    merge_sort(sublist2)
    merge(xlist, sublist1, sublist2)
    return


evil_characters = ["Pinochio", "Mickey Mouse", "Cinderella", "Bell",
                   "Jasmine", "Simba", "Buzz Lightyear", "Prince Eric",
                   "Daisy Duck", "Prince Charming", "Snow White", "Aladdin",
                   "Pocahontal", "Nemo", "Olaf", "Sheriff Woody", "Princess Aurora"]

merge_sort(evil_characters)
print(evil_characters)


# Quicksort

def quicksort(xlist):
    # handle base-case
    if len(xlist) <= 1:
        return

    # pick pivot
    pivot = xlist[0]

    # form gt/lt sublists
    listA = []
    listB = []

    for element in xlist[1:]:
        if element < pivot:
            listA.append(element)
        else:
            listB.append(element)

    # quicksort sublists
    quicksort(listA)
    quicksort(listB)

    # join sublists and pivot
    xlist[:] = []
    for element in listA:
        xlist.append(element)

    xlist.append(pivot)

    for element in listB:
        xlist.append(element)

    return


edc = ["Pinochio", "Mickey Mouse", "Cinderella", "Bell",
                   "Jasmine", "Simba", "Buzz Lightyear", "Prince Eric",
                   "Daisy Duck", "Prince Charming", "Snow White", "Aladdin",
                   "Pocahontal", "Nemo", "Olaf", "Sheriff Woody", "Princess Aurora"]

quicksort(edc)
print(edc)

